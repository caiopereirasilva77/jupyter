import pandas as pd
import numpy as np
desired_width = 320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)

df = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_pageviews.json",lines=True)

# fomartacao pra impressao de numeros inteiros e todas as colunas no terminal
#pd.options.display.float_format = "{:.2f}".format
pd.set_option('display.max_columns', None)

print(df.head())
df.info()

## Verificado no "prof_report_oline_pageviews.htmal"
# Dataset has 955883 duplicate rows Warning

#Removendo valores duplicados
df.duplicated()

# remove todos os valores repetidos.
#df.drop_duplicates()
df = df.drop_duplicates()
df.info()























#print(df.head())
#print(df.deviceType.value_counts())
#print(df.visitor_id.value_counts())
#print(df.customer_id.value_counts())

#print(df.date.unique())


#print(df.date.dt.to_period('M'))


#print(np.unique(df["date"].dt.strftime('%d-%m-%y')))

#print(df.date.dt.to_period('D'))

#df['dia_de_visita_online_pv'] = df.date.dt.to_period('D').astype(str)

#df.dia_de_visita_online_pv.head()

#df.head()

#visitas_por_dia_online_pv = df.groupby(by='dia_de_visita_online_pv').visitor_id.sum()

#visitas_por_dia_online_pv.head()

#visitas_por_dia_online_pv.index.item

#print(visitas_por_dia_online_pv.values)

#df['mes_de_visita_online_pv'] = df.date.dt.to_period('M').astype(str)

#df.mes_de_visita_online_pv.head()

#print(df.head())

#visitas_por_mes_online_pv = df.groupby(by='mes_de_visita_online_pv').visitor_id.sum()

#visitas_por_mes_online_pv.index.item


#a = visitas_por_mes_online_pv

#print("Total no",str(a))
#df.info()

#df.shape
#print(df[df.duplicated(keep='first')].shape)

#df[df.duplicated(subset=['date','visitor_id','deviceType','pageType','category_id','on_product_id','customer_id'], keep=False)].head()


