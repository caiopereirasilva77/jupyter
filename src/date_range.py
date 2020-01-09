import pyspark.sql.functions as func
from pyspark.shell import sqlContext
import pandas_profiling
from pyspark.sql.types import TimestampType

from datetime import datetime

df_y = sqlContext.read.json("C:/Users/cps_f/OneDrive/Documentos/Personal/Processo Selecao/Linx/offline_sales.json", lines=True)


udf_dt = func.udf(lambda x: datetime.strptime(x, '%Y%m%d%H%M%S'), TimestampType())

df = df_y.withColumn('datetime', udf_dt(df_y.date))

df_g = df_y.groupby(func.hour(df_y.date))

df_y.groupby(df_y.name).agg(func.countDistinct('address')).show()

pandas_profiling.ProfileReport(df)