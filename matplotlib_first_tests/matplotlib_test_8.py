from matplotlib import pyplot as plt
import numpy as np

def graph_data(stock):
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('interessting Graph\nCheck that out')
    plt.legend()
    plt.show()

graph_data('TSLA')