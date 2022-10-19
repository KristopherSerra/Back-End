from pyclbr import Function
import pandas as pd

# ------------------------------- FUNCIONES -------------------------------
# Une el cod. area y el bloque
def get_range(i):
    cod = str(location.iloc[i].INDICATIVO);
    block = str(location.iloc[i].BLOQUE)
    conc = cod + block
    return int(conc)


# ---------------------------------- MAIN ----------------------------------

book = pd.read_csv('rangos.csv')

# dataFrame con la info de la localidad pedida
location = book[book['LOCALIDAD'] == input('Ingrese localidad: ').upper()]

# Contiene el conjunto del codigo de area + el bloque
rangArray = [] 

for i in range(len(location)):
    rangArray.append(get_range(i))


# Almacena cuantos digitos faltan para completar el numero
faltantes = [] 
for i in range(len(rangArray)):
    faltantes.append(10 - len(str(rangArray[i])))

# Crear el numero
numeros = []




# print para test
for i in range(len(location)):
    print(rangArray[i])


# Importa el codigo de area y bloque en archivos separados (no requerido por ahora)

# codArea = location['INDICATIVO']
# bloque = location['BLOQUE']
# codArea.to_csv('codArea.csv', encoding='utf-8', index=False)
# bloque.to_csv('bloque.csv', encoding='utf-8', index=False)


