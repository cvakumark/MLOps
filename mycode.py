import os
import pandas as pd

data = {'Name': ['Siva', 'Kumar', 'Kalva'], 'Age': [30, 35, 45],
        'City': ['Nandyal', 'Katarukonda', 'Bangalore']
        }
df = pd.DataFrame(data)
new_row_loc = {'Name': 'Havisha', 'Age': 12, 'City': 'Blr'}
df.loc[len(df.index)] = new_row_loc
new_row_loc2 = {'Name': 'Likitha', 'Age': 15, 'City': 'Blr'}
df.loc[len(df.index)] = new_row_loc2
data_dir='data'
os.makedirs(data_dir, exist_ok=True)

file_path = os.path.join(data_dir, 'sample_data.csv')
df.to_csv(file_path, index=True)
print(f"CSV file save to {file_path}")