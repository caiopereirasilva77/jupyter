from load_file.load_offline_sales import fat_mes_offline
from load_file.load_online_orders import fat_mes_online_or
from load_file.load_offline_sales import fat_dia_offline
from load_file.load_online_orders import fat_dia_online_or

## 1 - faturamento total no periodo (mensal)
total_venda_por_mes: object = fat_mes_online_or + fat_mes_offline
print(total_venda_por_mes)
## faturamento total no periodo (diario)
total_venda_por_dia = fat_dia_offline + fat_dia_online_or
print('aqui',total_venda_por_dia)

