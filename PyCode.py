from statistics import mode
import sys
import os
import pandas as pd

xlFile = ''

if len(sys.argv) > 1:
    xlFile = sys.argv[1]
else:
    xlFile = r'E:/Albet Ubaidi/Python/Sales.xlsx'

# Sheet2
data_product = pd.read_excel(
    xlFile, sheet_name="Sheet2", index_col='Id', header=3).loc[:, 'Name':]

# Sheet1
data_sales = pd.read_excel(xlFile, sheet_name="Sheet1",
                           index_col="Id", header=3, ).loc[:, 'Store':]

# Menjumlahkan total Sales Sesuai Id
salesByProduct = data_sales.groupby('Product_Id').Sales.sum()
# Menambahkan data Qty Perproduct
qtysold = data_sales.groupby('Product_Id').Qty.sum()

# menambahkan kolom baru
data_product['Total_Sales'] = data_sales.groupby('Product_Id').Sales.sum()
data_product['Qty_Sold'] = data_sales.groupby('Product_Id').Qty.sum()
data_product['COGS'] = data_product.Purchase * data_product.Qty_Sold
data_product['Margin_Income'] = data_product.Total_Sales - data_product.COGS
data_product['Margin/Sales'] = data_product.Margin_Income / \
    data_product.Total_Sales

# Gabungkan dengan file Excel.. Append data_product to Excel
with pd.ExcelWriter(xlFile, mode='a') as w:
    data_product.to_excel(w, sheet_name="Report")

# print(data_product.head(10))
# print(data_sales.head(10))
# print(salesByProduct.head(10))

# Menambahkan total penjualan
print(data_product.head())

# Menampilkan Qty
# print(qtysold.head())
