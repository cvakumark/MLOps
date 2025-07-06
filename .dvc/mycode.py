import os
import pandas as pd

data = {'Name': ['Siva', 'Kumar', 'Kalva'], 'Age': ['30', '35', '45'],
        'City': ['Nandyal', 'Katarukonda', 'Bangalore']
        }
df = pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=True)
print(f"CSV file save to {file_path}")