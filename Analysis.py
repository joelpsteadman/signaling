import pandas as pd
from pandasql import sqldf


df = pd.read_csv('database.csv')

# print(df.head(10))
# print(df.info()) 

query = "SELECT Sex, Quality \
        FROM df\
        WHERE Generation == 50"

df_orders = sqldf(query)
print(df_orders.head(50))
