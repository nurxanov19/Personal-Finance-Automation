import streamlit as st
import plotly.express as px
import pandas as pd
import json, os
from config import (
    CATEGORY_FILE,
    DATE_COLUMN,
    DESCRIPTION_COLUMN,
    AMOUNT_COLUMN,
    CATEGORY_COLUMN,
    CURRENCY_COLUMN,
    ACCOUNT_COLUMN,
)

# Setup Streamlit
st.set_page_config(page_title="Finance Dashboard", page_icon='$', layout='wide')

category_file = CATEGORY_FILE

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
        df[AMOUNT_COLUMN] = df[AMOUNT_COLUMN].str.replace(',', '', regex=False).astype(float)
        df[DATE_COLUMN] = pd.to_datetime(df[DATE_COLUMN], format="%d/%m/%Y")
        
        # Handle empty categories
        df[CATEGORY_COLUMN] = df[CATEGORY_COLUMN].fillna('Uncategorized')
        
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
            expenses_df = df[df[AMOUNT_COLUMN] < 0].copy()
            income_df = df[df[AMOUNT_COLUMN] > 0].copy()
            
            # Make the amount positive for display
            expenses_df[AMOUNT_COLUMN] = expenses_df[AMOUNT_COLUMN].abs()

            st.session_state.expenses_df = expenses_df.copy()

            tab1, tab2 = st.tabs(['Expenses', 'Income'])
            with tab1:
                st.subheader('Your Expenses')

                categories = ["All"] + list(st.session_state.categories.keys())
                selected_categories = st.multiselect("Filter by category", categories, default=["All"])

                if "All" in selected_categories:
                    filtered_expenses_df = st.session_state.expenses_df
                else:
                    filtered_expenses_df = st.session_state.expenses_df[st.session_state.expenses_df[CATEGORY_COLUMN].isin(selected_categories)]

                edited_df = st.data_editor(
                    filtered_expenses_df[[DATE_COLUMN, DESCRIPTION_COLUMN, AMOUNT_COLUMN, CATEGORY_COLUMN, ACCOUNT_COLUMN]],
                    column_config={
                        DATE_COLUMN: st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
                        DESCRIPTION_COLUMN: "Description",
                        AMOUNT_COLUMN: st.column_config.NumberColumn("Amount", format=f"%.2f {expenses_df[CURRENCY_COLUMN].iloc[0]}"),
                        CATEGORY_COLUMN: st.column_config.SelectboxColumn(
                            "Category",
                            options=list(st.session_state.categories.keys())
                        ),
                        ACCOUNT_COLUMN: "Account",
                    },
                    hide_index=True,
                    use_container_width=True,
                    key="category_editor"
                )

                save_button = st.button("Apply Changes", type="primary")
                if save_button:
                    st.session_state.expenses_df = edited_df.copy()
                        
                st.subheader('Expense Summary')
                category_totals = filtered_expenses_df.groupby(CATEGORY_COLUMN)[AMOUNT_COLUMN].sum().reset_index()
                category_totals = category_totals.sort_values(AMOUNT_COLUMN, ascending=False)
                
                st.dataframe(
                    category_totals, 
                    column_config={
                     AMOUNT_COLUMN: st.column_config.NumberColumn("Amount", format=f"%.2f {expenses_df[CURRENCY_COLUMN].iloc[0]}")   
                    },
                    use_container_width=True,
                    hide_index=True
                )
                
                fig = px.pie(
                    category_totals,
                    values=AMOUNT_COLUMN,
                    names=CATEGORY_COLUMN,
                    title="Expenses by Category"
                )
                st.plotly_chart(fig, use_container_width=True)

                st.subheader("Expenses by Account")
                account_totals = filtered_expenses_df.groupby(ACCOUNT_COLUMN)[AMOUNT_COLUMN].sum().reset_index()
                fig2 = px.pie(
                    account_totals,
                    values=AMOUNT_COLUMN,
                    names=ACCOUNT_COLUMN,
                    title="Expenses by Account"
                )
                st.plotly_chart(fig2, use_container_width=True)

                st.subheader("Daily Expenses")
                daily_expenses = filtered_expenses_df.groupby(DATE_COLUMN)[AMOUNT_COLUMN].sum()
                st.line_chart(daily_expenses)

                with st.expander("Add New Category"):
                    new_category = st.text_input("New Category Name")
                    if st.button("Add Category"):
                        if new_category and new_category not in st.session_state.categories:
                            st.session_state.categories[new_category] = []
                            save_categories()
                            st.rerun()

            with tab2:
                st.subheader("Income Summary")
                total_income = income_df[AMOUNT_COLUMN].sum()
                st.metric("Total Income", f"{total_income:,.2f} {income_df[CURRENCY_COLUMN].iloc[0]}")

                st.write(income_df)    
        
main()
