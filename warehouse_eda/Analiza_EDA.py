import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    'ID': [1, 2, 3, 4, 5, 6, 7],
    'Model': ['HP EliteBook', 'Lenovo ThinkPad', 'HP EliteBook', 'Dell Latitude', 'Apple MacBook', 'Lenovo ThinkPad', 'Asus VivoBook'],
    'Cena_PLN': [4500, 5200, 4500, np.nan, 8500, 5200, 3100],
    'Typ': ['biznesowy', 'biznesowy', 'biznesowy', 'biurowy', 'graficzny', 'biznesowy', 'domowy']
}

df = pd.DataFrame(data)


df.to_csv('magazyn_dane.csv', index=False)
print("Plik magazyn_dane.csv został wygenerowany!")


df = pd.read_csv('magazyn_dane.csv')


srednia = df['Cena_PLN'].mean()


df['Cena_PLN'] = df['Cena_PLN'].fillna(srednia)

print("\n--- PO SPRZĄTANIU ---")
print(df.isnull().sum())


print("\n--- CZY MAMY BRAKUJĄCE DANE? ---")
print(df.isnull().sum())


print("\n--- ILE MAMY POWTÓREK? ---")
print(f"Liczba zduplikowanych wierszy: {df.duplicated().sum()}")


print("\n--- STATYSTYKI CEN ---")
print(df['Cena_PLN'].describe())


plt.bar(df['Model'], df['Cena_PLN'], color='skyblue')


plt.xlabel('Model Laptopa')
plt.ylabel('Cena w PLN')
plt.title('Porównanie cen sprzętu w magazynie')
plt.xticks(rotation=45)

# wykres
plt.tight_layout()
plt.show()

# średnia cena dla każdej grupy
analiza_typu = df.groupby('Typ')['Cena_PLN'].mean().sort_values(ascending=False)

print("\n--- ŚREDNIA CENA W ZALEŻNOŚCI OD TYPU ---")
print(analiza_typu)
# Filtrowanie1
drogie_laptopy = df[df['Cena_PLN'] > 5000]

print("\n--- SPRZĘT PREMIUM (POWYŻEJ 5000 PLN) ---")
print(drogie_laptopy[['Model', 'Cena_PLN']])

# Filtrowanie tekstowe
tylko_hp = df[df['Model'].str.contains('HP')]

print("\n--- LISTA SPRZĘTU MARKI HP ---")
print(tylko_hp)

# wykres kołowy
analiza_typu.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='Pastel1')
import matplotlib.pyplot as plt
plt.title('Udział typów sprzętu w budżecie (średnio)')
plt.ylabel('')
plt.show()