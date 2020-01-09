# jupyter
O app, foi extrutura em 3 pastas, conforme figura acima:
•	Extrator : Faz o load do arquivo e gera relatorio profile utilizando a biblioteca profile-pandas
Obs: na extracao do arquivo ‘online_pagevies.json’ foi realizada diretamente no ambiente google colab notebook, por conta da performance.
•	Load File: Carrega os arquivos json, faz formatação de datatype e gera arquivo em formato csv para futura carga no Powerbi
•	Plot:  Geracao de gráfico
Obs: não implementada na integra.
•	Arquivos:
•	Consolidacao_vendas.py: realizada o import dos arquivos load_, permitindo realizar a consolidação das vendas offline e online
•	Merge_online_sales _and_online_pageviews: realizada merge entre os dataframes utilizando como chave o atributo customer_id
