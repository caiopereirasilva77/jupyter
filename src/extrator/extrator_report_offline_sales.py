import pandas as pd
import pandas_profiling

df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/offline_sales.json",lines=True)

report = pandas_profiling.ProfileReport(df)
report.to_file('prof_report_offline_sales.html')
