import pandas as pd
url = 'http://canisius.edu/~yany/data/ibm.csv'
x = pd.read_csv(url)
print(x.head())