import pandas as pd
import numpy as np

bostondata=pd.read_csv("boston.csv")
print(bostondata)

bostondata.boxplot()
bostondata.plot.scatter(x='NOX', y='DIS')