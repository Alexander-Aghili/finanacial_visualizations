import matplotlib.pyplot as plt
from datetime import datetime

def plot_net_income_over_time(fin_data, company, period):
    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in fin_data]
    net_income = [entry["netincomeloss"] for entry in fin_data]
    plt.figure(figsize=(10, 5))
    plt.bar(dates, net_income, width=100, color='red')
    plt.title(company + ' Net Income Per ' + period)
    plt.xlabel('Date')
    plt.ylabel('Net Income')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig(company + 'NetIncome.png')


