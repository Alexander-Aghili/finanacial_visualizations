import requests
import json

def get_financial_data(api_key, symbol, period='annual', limit=50):
    """
    Fetches the financial statement data for a given company symbol.

    :param api_key: Your API key for the Financial Modeling Prep API.
    :param symbol: The stock symbol of the company (e.g., AAPL for Apple).
    :param period: The period for the financial data (default is 'annual').
    :param limit: The number of results to return (default is 50).
    :return: A dictionary containing the financial data.
    """
    url = f'https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/{symbol}?period={period}&limit={limit}&apikey={api_key}'
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()

if __name__ == "__main__":
    # Replace 'your_api_key' with your actual API key
    api_key = 'TImFCmFei1Oo7dISNpGsNWu78WGgIv6L'
    company_symbol = 'AAPL'  # Replace with any company's stock symbol you want to fetch data for

    try:
        financial_data = get_financial_data(api_key, company_symbol)
        print(json.dumps(financial_data, indent=4))
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'An error occurred: {err}')

