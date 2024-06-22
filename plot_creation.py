import matplotlib.pyplot as plt
from datetime import datetime

def plot_bar_data(dates, data, ylabel, company, period):
    plt.figure(figsize=(10, 5))
    plt.bar(dates, data, width=100, color='red')
    plt.title(company + ' ' + ylabel + ' Per ' + period)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('./images/' + company + ylabel.replace(" ", "") + '.png')

def plot_data(dates, data, ylabel, company, period):
    plt.figure(figsize=(10,5))
    plt.plot(dates, data, marker='o')
    plt.title(company + ' ' + ylabel + ' Per ' + period)
    plt.xlabel('Date')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('./images/' + company + ylabel.replace(" ", "") + '.png')



def plot_net_income_over_time(fin_data, company, period):
    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in fin_data]
    net_income = [entry["netincomeloss"] for entry in fin_data]
    plot_bar_data(dates, net_income, 'Net Income', company, period)

def plot_gross_profit(fin_data, company, period):
    dates = [datetime.strptime(entry["date"], "%Y-%m-%d") for entry in fin_data]
    gross = [entry["operatingincomeloss"] for entry in fin_data]
    plot_bar_data(dates, gross, 'Gross Profit', company, period)

