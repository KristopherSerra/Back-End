from pyclbr import Function
import pandas as pd

# ------------------------------- FUNCIONES -------------------------------
# Une el cod. area y el bloque
def get_range(i):
    cod = str(location.iloc[i].INDICATIVO);
    block = str(location.iloc[i].BLOQUE)
    conc = cod + block
    return conc


#Crea la parte faltante del numero
def createNumber(l,f, i):
    if (l != 0):
        start = l*(10**f)
        end = ((l+1)*(10**f))-1
        for j in range(start, end):
            rango = str(rangoCompleto[i][:-1])
            rest = str(j)
            numerosPosibles.append(rango + rest) 
# ---------------------------------- MAIN ----------------------------------

book = pd.read_csv('rangos.csv')

# dataFrame con la info de la localidad pedida
location = book[book['LOCALIDAD'] == input('Ingrese localidad: ').upper()]

# Contiene el conjunto del codigo de area + el bloque
rangoCompleto = [] 

for i in range(len(location)):
    rangoCompleto.append(get_range(i))


# Almacena cuantos digitos faltan para completar el numero
faltantes = [] 
for i in range(len(rangoCompleto)):
    faltantes.append(10 - len(str(rangoCompleto[i])))

# Crear el numero
numerosPosibles = []
for i in range(len(rangoCompleto)):
    createNumber(int(rangoCompleto[i][-1]), int(faltantes[i]), i)

pd.DataFrame(numerosPosibles).to_csv("numeros.csv")


#for i in range(len(rangoCompleto)):
#    print(rangoCompleto[i])




