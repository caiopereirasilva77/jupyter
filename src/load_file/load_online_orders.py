import pandas as pd
import numpy as np
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)


df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_orders.json",lines=True)
df['date'] = pd.to_datetime(df['date'])
df['price_total_online_or'] = df.quantity * df.price

fat_mes_online_or = df.groupby(df['date'].dt.strftime('%B'))['price_total_online_or'].sum().sort_index()
fat_dia_online_or = df.groupby(df['date'].dt.strftime('%B %d, %Y'))['price_total_online_or'].sum().sort_index()



# fomartacao pra impressao de todas as colunas no terminal
pd.set_option('display.max_columns', None)

print(df.head())
df.info()

## 2 - produto mais vendido

#print(df.on_product_id.value_counts())
##  O produto mais comprado on line é o de 'on_product_id' = 626664333563363 com 74 unidades
##626664333563363    74

## retorna o indice mais vendido
#df = df.groupby('on_product_id')['quantity'].sum().idxmax()
#print(df)
# 626664333563363

# geracao de arquivo csv do dataframe para carga no powerbi
df.to_csv(r'C:\Users\cps_f\OneDrive\Documentos\Personal\Processo Selecao\Linx\online_orders_ed.csv', sep='\t', encoding='utf-8', header='true')

# 3. Cariocas gostam de comprar no fim de semana?

# - Temos:
# - 1723 Cariocas que compram offline no final de semana
# - 7142 Cariocas que compram offline nos dias de semana

#Foi realizado merge no powerbi entre os dataframes (online_orders e offline_sales), pra sabermos, quais são os clientes online , são cariocas.
# Temos: 970 Cariocas no dataframe.

# Como, do Dateframe offline de um total de 8865 (1723 + 7142), temos apenas 1723 Cariocas gostam de comprar no final de semana e do Dataframe online temos um total de 970
# cariocas, matematicamente é impossível que considerando os cariocas "online" que compram somente no final de semana, tenhamos um numero superior ao Cariocas que compram nos dias de
# semana.
# Logo podemos inferir que os cariocas gostam de comprar nos dias de semana e não aos finais de semana.


























#print(df.groupby(df['date'].dt.strftime('%B'))['price_total_online_or'].sum().sort_index())
#print(df.head())

#pandas_profiling.ProfileReport(beers_and_breweries)
#print(df.deviceType.value_counts())



#print(df.date.unique())
#print(df.quantity.unique())
#print(df.quantity == 2)
#print(df.quantity[df.quantity == 2])

#print(df.date.dt.to_period('M'))

#print(np.unique(df["date"].dt.strftime('%d-%m-%y')))

#print(df.date.dt.to_period('D'))

#df['dia_de_faturamento_online_or'] = df.date.dt.to_period('D').astype(str)

#df.dia_de_faturamento_online_or.head()

#df.head()


#df['price_total_online_or'] = df.quantity * df.price


#def vendas_por_dia_online_or(self):

  #  a = Online_orders().getVendas_por_dia_online_or()

#vendas_por_dia_online_or = df.groupby(by='dia_de_faturamento_online_or').price_total_online_or.sum()


#print(vendas_por_dia_online_or)

#vendas_por_dia_online_or.head()

#a.vendas_por_dia_online_or.index.item

#print(vendas_por_dia_online_or.values)

#df['mes_de_faturamento_online_or'] = df.date.dt.to_period('M').astype(str)

#df.mes_de_faturamento_online_or.head()

#print(df.head())

#vendas_por_mes_online_or = df.groupby(by='mes_de_faturamento_online_or').price_total_online_or.sum()

#endas_por_mes_online_or.index.item


#b = Online_orders(vendas_por_mes_online_or)


#setattr(a, 'vendas_por_mes_online_or', vendas_por_mes_online_or)

#a = vendas_por_mes_online_or
#b = vendas_por_dia_online_or
#print("Total no",str(a))
#print("Total no",str(b))

#df.info()