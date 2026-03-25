import pandas as pd
data=[10,20,30]
labels=['a','b','c']
series=pd.series(data,index=labels)
print("pandas series")
print(series)
print("value at label b:",series['b'])