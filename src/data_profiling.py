import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

offline_sales = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/offline_sales.json",lines=True)
online_orders = pd.read_json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/online_orders.json",lines=True)


data_set = pd.merge(offline_sales,
                    online_orders,
                    how='inner',
                    left_on="sale_id",
                    right_on="order_id",
                    sort=True,
                    suffixes=('_offiline', '_online'))

offline_sales.dtypes

def get_var_category(series):


    unique_count = series.nunique(dropna=False)
    total_count = len(series)
    if pd.api.types.is_numeric_dtype(series):
        return 'Numerical'
    elif pd.api.types.is_datetime64_dtype(series):
        return 'Date'
    elif unique_count==total_count:
        return 'Text (Unique)'
    else:
        return 'Categorical'

def print_categories(pd):
    for column_name in pd.columns:
        print(column_name, ": ", get_var_category(pd[column_name]))

print_categories(offline_sales)

length = len(offline_sales["price"])
print(length)

count = offline_sales["price"].count()
print(count)

number_of_missing_values = length - count
pct_of_missing_values = float(number_of_missing_values / length)
pct_of_missing_values = "{0:.1f}%".format(pct_of_missing_values*100)
print(pct_of_missing_values)

print("Minimum value: ", offline_sales["price"].min())
print("Maximum value: ", offline_sales["price"].max())

print(offline_sales["price"].mode())

mean = offline_sales["price"].mean()
median = offline_sales["price"].median()

standarddev = offline_sales["price"].std()

quantile = offline_sales["price"].quantile([.25, .5, .75])


sns.set(color_codes=True)
sns.set_palette(sns.color_palette("muted"))

sns.distplot(offline_sales["price"].dropna())
plt.show()

#offline_sales.info()

offline_sales[["store_id", "sale_id", "off_product_id","quantity","customer_id"]].corr()
#offline_sales[["name", "style"]].describe()