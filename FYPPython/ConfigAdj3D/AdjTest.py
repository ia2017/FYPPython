import pandas as pd

f_history1 = pd.read_csv('history_1.csv')
f_history1.columns = f_history1.columns.str.replace('"', '')
print(f_history1.columns)