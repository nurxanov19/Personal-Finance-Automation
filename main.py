import streamlit as st
import plotly.express as px
import pandas as pd
import json, os

# Setup Streamlit
st.set_page_config(page_title="Finance App", page_icon='$', layout='wide')

category_file = 'categories.json'

if 'categories' not in st.session_state:
    st.session_state.categories = {
        "Uncategorized": []
    }

if os.path.exists(category_file):
    with open(category_file, 'r') as f:
        st.session_state.categories = json.load(f)

def save_categories():
    with open(category_file, 'w') as f:
        json.dump(st.session_state.categories, f)

def load_transactions(file):
    try:
        df = pd.read_csv(file)
        df.columns = [col.strip().lower() for col in df.columns]
        df["amount"] = df["amount"].str.replace(',', '', regex=False).astype(float)
        df["date"] = pd.to_datetime(df['date'], format="%d/%m/%Y")
        
        # Handle empty categories
        df['category'] = df['category'].fillna('Uncategorized')
        
        return df

    except Exception as e:
        st.error(f'Error processing file: {str(e)}')
        return None

def main():
    st.title("Finance Dashboard")
    
    uploaded_file = st.file_uploader(label="Upload your Monefy data as a csv file", type=['csv'])
    
    if uploaded_file is not None:
        df = load_transactions(uploaded_file)

        if df is not None:
            # Expenses are negative, income is positive
            expenses_df = df[df['amount'] < 0].copy()
            income_df = df[df['amount'] > 0].copy()
            
            # Make the amount positive for display
            expenses_df['amount'] = expenses_df['amount'].abs()

            st.session_state.expenses_df = expenses_df.copy()

            tab1, tab2 = st.tabs(['Expenses', 'Income'])
            with tab1:
                st.subheader('Your Expenses')
                
                # The columns in the new CSV are different.
                # Let's use 'date', 'description', 'amount', 'category'.
                # The original file had 'Details', which we'll replace with 'description'.
                edited_df = st.data_editor(
                    st.session_state.expenses_df[['date', 'description', 'amount', 'category']],
                    column_config={
                        "date": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        "description": "Description",
                        "amount": st.column_config.NumberColumn("Amount", format=f"%.2f {expenses_df['currency'].iloc[0]}"),
                        "category": st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        )
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    # The logic to add keywords is no longer needed.
                    # We just update the dataframe in the session state.
                    st.session_state.expenses_df = edited_df.copy()
                        
                st.subheader('Expense Summary')
                category_totals = st.session_state.expenses_df.groupby("category")["amount"].sum().reset_index()
                category_totals = category_totals.sort_values("amount", ascending=False)
                
                st.dataframe(
                    category_totals, 
                    column_config={
                     "amount": st.column_config.NumberColumn("Amount", format=f"%.2f {expenses_df['currency'].iloc[0]}")   
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                fig = px.pie(
                    category_totals,
                    values="amount",
                    names="category",
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

                with st.expander("Add New Category"):
                    new_category = st.text_input("New Category Name")
                    if st.button("Add Category"):
                        if new_category and new_category not in st.session_state.categories:
                            st.session_state.categories[new_category] = []
                            save_categories()
                            st.rerun()

            with tab2:
                st.subheader("Income Summary")
                total_income = income_df["amount"].sum()
                st.metric("Total Income", f"{total_income:,.2f} {income_df['currency'].iloc[0]}")

                st.write(income_df)    
        
main()