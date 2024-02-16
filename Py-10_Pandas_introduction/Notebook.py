import pandas as pd 
pd.__version__


melb_data = pd.read_csv('Py-10_Pandas_introduction\data\countries.csv',sep= ';')
a = melb_data.tail(3)
print(a)