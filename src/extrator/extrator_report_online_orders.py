import pandas as pd
import pandas_profiling

df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_orders.json",lines=True)

report = pandas_profiling.ProfileReport(df)
#df.customer_id = df.index.astype(str)
#df.info()
report.to_file('prof_report_online_orders.html')
