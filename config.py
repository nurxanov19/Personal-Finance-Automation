# Configuration for the Personal Finance Dashboard

import locale   # for handling large numbers by formatting 120000 -> 120,000
# File paths
CATEGORY_FILE = "categories.json"

# Column names
DATE_COLUMN = "date"
DESCRIPTION_COLUMN = "description"
AMOUNT_COLUMN = "amount"
CATEGORY_COLUMN = "category"
CURRENCY_COLUMN = "currency"
ACCOUNT_COLUMN = "account"

try: 
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'English_United States')

    except locale.Error:
        print("Locale setting failed, using default formatting")
        