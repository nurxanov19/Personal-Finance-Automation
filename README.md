# Personal Finance Dashboard

## Project Overview

This project provides a simple yet effective personal finance dashboard built with Python and Streamlit. It is designed to help users visualize and analyze their financial transactions exported from Monefy. By uploading a CSV export from Monefy, users can gain insights into their spending habits and income streams through interactive charts and tables. The application also supports dynamic categorization of expenses, allowing for a personalized view of financial data.

## Features

-   **Monefy CSV Upload:** Easily upload your transaction data exported from the Monefy application.
-   **Interactive Data Visualization:** View your income and expenses through dynamic tables and pie charts powered by Plotly.
-   **Expense Categorization:** Categorize your transactions using a customizable list of expense categories. New categories can be added directly within the application.
-   **Income and Expense Summary:** Get a clear overview of your total income and a breakdown of expenses by category.
-   **Dynamic Currency Display:** The application automatically detects and displays the currency from your uploaded data.

## Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install streamlit pandas plotly
    ```

## Usage

1.  **Run the Streamlit application:**
    ```bash
    streamlit run main.py
    ```

2.  **Access the Dashboard:**
    Once the application starts, it will open in your default web browser (usually at `http://localhost:8501`).

3.  **Upload Your Data:**
    On the dashboard, use the "Upload your Monefy data as a csv file" uploader to select your Monefy export file (e.g., `Monefy.Data.23-12-2025.csv`).

4.  **Explore Your Finances:**
    The dashboard will display two tabs: "Expenses" and "Income".
    -   **Expenses Tab:** View a data editor for your expenses, an expense summary by category, and a pie chart visualization. You can also add new expense categories here.
    -   **Income Tab:** See a summary of your total income and a detailed table of income transactions.

## Project Structure

```
.
├── main.py                     # Main Streamlit application file
├── categories.json             # JSON file storing expense categories
├── Monefy.Data.23-12-2025.csv  # Example Monefy data export (CSV)
└── README.md                   # Project README file
```

-   `main.py`: Contains the core logic for the Streamlit application, including data loading, processing, visualization, and user interface elements.
-   `categories.json`: Stores a dictionary of expense categories. This file is dynamically updated when new categories are added through the UI.
-   `Monefy.Data.23-12-2025.csv`: A sample CSV file demonstrating the expected format of a Monefy data export.

## Contributing

Contributions are welcome! If you have suggestions for improvements, new features, or bug fixes, please open an issue or submit a pull request.

## License

This project is open-source and available under the [MIT License](LICENSE).
