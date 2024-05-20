import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo excel
file_path = 'sales_data.xlsx' 
df = pd.read_excel(file_path)

# Agrupar por produto e calcular o total de unidades vendidas para cada produto.
product_sales = df.groupby('product')['units_sold'].sum().reset_index()

# Organizar por ordem decrescente de vendas.
top_products = product_sales.sort_values(by='units_sold', ascending=False).head(5)

# top 5 mais vendidos
plt.figure(figsize=(10, 6))
plt.bar(top_products['product'], top_products['units_sold'], color='skyblue')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.title('Top 5 Best Selling Products')
plt.xticks(rotation=45)
plt.tight_layout()

# Visualizar o gráfico
plt.show()
