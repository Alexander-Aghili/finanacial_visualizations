from data import get_financial_data
from plot_creation import plot_net_income_over_time


def plot_all_companies(companies):
    period = "Year"
    for company in companies:
        fin_data = get_financial_data(company)
        plot_net_income_over_time(fin_data, company, period)


companies = ['AAPL', 'AMZN', 'TSLA', 'NVDA', 'MSFT', 'GOOG']
plot_all_companies(companies)
