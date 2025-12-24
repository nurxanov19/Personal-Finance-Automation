# Personal Finance Dashboard

## Project Overview

This project is a personal finance dashboard application built using Python and the Streamlit framework. Its primary purpose is to help users visualize and analyze their financial transactions by importing data exported from the Monefy application. It provides interactive features for understanding spending habits, income streams, and allows for dynamic categorization of expenses.

**Key Technologies:**
- Python
- Streamlit
- Pandas (for data manipulation)
- Plotly Express (for interactive visualizations)

## Building and Running

**Dependencies:**
The project requires the following Python packages: `streamlit`, `pandas`, `plotly`.

**Installation:**
1.  **Clone the repository:**
    ```bash
    git clone https://github.com/nurxanov19/Personal-Finance-Automation.git
    cd "Personal Finance Automation"
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```
3.  **Install the required packages:**
    ```bash
    pip install streamlit pandas plotly
    ```

**Running the Application:**
To start the finance dashboard, execute the following command in your terminal:
```bash
streamlit run main.py
```
The application will open in your web browser, typically at `http://localhost:8501`.

## Development Conventions

-   **Framework:** Streamlit is used for building the interactive web application.
-   **Data Handling:** Pandas is extensively used for loading, cleaning, and manipulating financial data from CSV files.
-   **Visualization:** Plotly Express is employed for generating various interactive charts (pie charts, line charts) to represent financial data.
-   **Configuration:** Key application settings and column names are managed in `config.py` for easy modification and maintenance.
-   **Expense Categorization:** Categories are stored in `categories.json` and can be managed directly within the application's UI.

## Project Structure

-   `main.py`: The core Streamlit application script orchestrating data loading, processing, UI rendering, and interaction logic.
-   `config.py`: Contains configuration variables such as file paths and column names, centralizing configurable aspects of the application.
-   `categories.json`: A JSON file that stores the user-defined expense categories. This file is dynamically updated by the application.
-   `Monefy.Data.23-12-2025.csv`: A sample CSV file providing an example of the expected data format for Monefy exports.
-   `README.md`: Provides a general overview, setup instructions, and usage guide for the project.
-   `GEMINI.md`: (This file) Serves as an instructional context for AI interactions, detailing the project's technical aspects and conventions.
