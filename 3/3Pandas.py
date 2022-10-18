import pandas as pd

book = pd.read_csv('rangos.csv')

location = book[book['LOCALIDAD'] == input('ingrese localidad: ')]
print('\n NUMEROS DE PILAR  :\n', location)

