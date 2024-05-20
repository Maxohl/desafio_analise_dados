import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Seed para reprodução
random.seed(42)
np.random.seed(42)

# Definir nome de produtos e outras constantes
product_names = ["Product A", "Product B", "Product C", "Product D", "Product E"]
num_entries = 20
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

# Gerar informação aleatória
data = {
    "product_id": [i + 1 for i in range(num_entries)],
    "product": [random.choice(product_names) for _ in range(num_entries)],
    "price": np.round(np.random.uniform(10, 100, num_entries), 2),
    "units_sold": np.random.randint(1, 20, num_entries),
    "date": [start_date + timedelta(days=random.randint(0, (end_date - start_date).days)) for _ in range(num_entries)]
}

# Criar uma DataFrame
df = pd.DataFrame(data)

# Salvar como arquivo excel.
file_path = 'sales_data.xlsx'
df.to_excel(file_path, index=False)

print(f"File '{file_path}' created successfully with random data.")
