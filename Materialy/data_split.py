import pandas as pd
from sklearn.model_selection import train_test_split

# Wczytanie danych z pliku CSV
data = pd.read_csv('lokata.csv')

# Podział danych na zbiory treningowy i testowy
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Zapisanie zbiorów do nowych plików CSV
train_data.to_csv('train_data.csv', index=False)
test_data.to_csv('test_data.csv', index=False)
