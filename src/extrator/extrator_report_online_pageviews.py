import pandas as pd
import pandas_profiling

df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_pageviews.json",lines=True)

report = pandas_profiling.ProfileReport(df)

# a geracao do arquivo em maquina local leva tempo demasiado, logo esse arquivo foi gerado no ambiente colab notebook
report.to_file('prof_report_online_pageviews.html')