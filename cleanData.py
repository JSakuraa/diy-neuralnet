import pandas as pd
import numpy as np

df = pd.read_csv('pokemon.csv')

df['total'] = df['hp'] + df['attack'] + df['defense'] + df['sp_attack'] + df['sp_defense'] + df['speed']

new_df = df[['name', 'total', 'capture_rate', 'is_legendary']].copy()

# 
new_df['total_new'] = df['total'] - df['total'].mean()

new_df['capture_rate_new'] = df['capture_rate'] - df['capture_rate'].mean()

selected_names = ['Weedle', 'Charmander', 'Starly', 'Mewtwo', 'Dialga']
selected_rows = new_df[new_df['name'].isin(selected_names)]

print(selected_rows)