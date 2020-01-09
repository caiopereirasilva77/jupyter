import pandas as pd
import numpy as np
import pandas_profiling

df1 = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_orders.json",lines=True)

df2 = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_pageviews.json",lines=True)

df3 = pd.merge(df1, df2, on='customer_id')
#print("Total no",str(a) + str(c))