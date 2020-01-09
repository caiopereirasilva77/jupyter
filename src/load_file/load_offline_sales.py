import pandas as pd
import numpy as np
# cofiguração do terminal output pra visualizarmos todas as colunas do dataframe ao imprimir no terminal
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)

#load do arquivo do drive_local
df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/offline_sales.json",  lines=True)

df['date'] = pd.to_datetime(df['date'])

# criacao de atributo preco total offline (quantity * price)
df['price_total_os'] = df.quantity * df.price

#criacao de atributo faturamento mensal offline agrupando e filtrando por mes e realizando a soma da coluna preco total offline
fat_mes_offline = df.groupby(df['date'].dt.strftime('%B'))['price_total_os'].sum().sort_index()
#criacao de atributo faturamento diario offline agrupando e filtrando por dia e realizando a soma da coluna preco total offline
fat_dia_offline = df.groupby(df['date'].dt.strftime('%B %d, %Y'))['price_total_os'].sum().sort_index()

print(fat_mes_offline)
print(fat_dia_offline)

# fomartacao pra impressao de numeros inteiros
pd.options.display.float_format = "{:.2f}".format
pd.set_option('display.max_columns', None)
print(df.head())
df.info()

#geracao de arquivo de csv para carga no powerbi
df.to_csv(r'C:\Users\cps_f\OneDrive\Documentos\Personal\Processo Selecao\Linx\offline_sales_ed.csv', sep='\t', encoding='utf-8', header='true')
