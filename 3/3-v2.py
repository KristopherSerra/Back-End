import pandas as pd

# ------------------------------- FUNCIONES -------------------------------

#Crea la parte faltante del numero
  
# --------------------------------------------------------------------------


# ---------------------------------- MAIN ----------------------------------
print("\033[H\033[J", end="")

rangos = pd.read_csv('rangos.csv')

# dataFrame con la info de la localidad pedida
loc = input('Ingrese localidad: ').upper()
if (loc in set(rangos["LOCALIDAD"])):
    location = rangos[rangos['LOCALIDAD'] == loc]
else:
    print("No se ha encontrado la localidad ingresada")
    print("Finalizando...")
    quit()


# Contienen el conjunto del codigo de area + el bloque
codArea = []
bloque = [] 

for i in range(len(location)):
    codArea.append(str(location.iloc[i].INDICATIVO))
    bloque.append(str(location.iloc[i].BLOQUE))
print("Datos de la locacion cargados exitosamente")    

# Almacena cuantos digitos faltan para completar el numero
faltantes = [] 
for i in range(len(bloque)):
    faltantes.append(10 - (len(str(codArea[i])) + len(str(bloque[i]))))

print("Se han realizado todos los pre-calculos necesarios")
print("Iniciando la creacion, aguarde un momento...")


# Crear el numero
numeros = []
for i in range(len(faltantes)):

    start = int(bloque[i])*(10**faltantes[i])
    if (int(bloque[i]) >= 100):
        end = ((int(bloque[i])+1)*(10**faltantes[i]))
    else:
        end = ((int(bloque[i])+10)*(10**faltantes[i]))

    #Prints de testing
    #print("Calculo del intervalo finalizados:")
    #print("Start = " , start)
    #print("End = " , end)
    #print("Bloque = " , bloque[i])
    #print("Faltantes = " , faltantes[i])


    for j in range(start, end):
        numeros.append(str(codArea[i]) + str(j)) 


print("Creacion de los numeros finalizada exitosamente")
print("Exportando...")


pd.DataFrame(numeros).to_csv("numeros.csv", index=False)



