import numpy as np
import pandas as pd
data=pd.read_csv(r"C:\Users\PRAVEEN\OneDrive\Desktop\supermarket_sales_inr_10000.csv",encoding="utf-8")
print(data)


# total_count=data.shape[0]
# print('total_count',total_count)
# print(data)

# print(data.isnull().sum())
print(data.info())###show the data type
# print(data.describe()) ##show the count mean std  min max
print(data)


###total _sales
data['Unit Price']=data['Unit_Price_INR'].astype(float)##change the data type and show the unit price
data['Quantity']=data['Quantity'].astype(int)##change the data type 
print(data)

# data['Total_sales']= data['Unit_Price_INR']* data['Quantity'] ##show the total sales
 
# print(data)

# # ##gross margin%
# data['profit margin']=(data["Gross_Income_INR"]/data['Total_sales'])*100
# print(data)

# # ##removeing null data
# data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# data['Month'] = data['Date'].dt.month_name()##split date column and give the value only month
# data['Year'] = data['Date'].dt.year##split date column and give the value only year
# data['Day'] = data['Date'].dt.day##split date column and give the value only date
# data = data.dropna(subset=['Date'])


# print(data)

# from sqlalchemy import create_engine
# username="root"
# password="root"
# host="localhost"
# port="3306"
# database="supermarketproject"

# engine=create_engine(f"mysql+pymysql://root:root@localhost:3306/supermarketproject")
# table_name="supermarketproject"
# data.to_sql(table_name,engine,if_exists="replace",index=False)