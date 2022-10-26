from time import sleep
import pandas as pd
import mysql.connector


# Console Clear
print("\033[H\033[J", end="")

#Export del archivo que contiene los rangos
rangos = pd.read_csv('rangos.csv')

# Creacion del DataFrame con la info de la localidad pedida
loc = input('Ingrese localidad: ').upper()

# Chequeo para verificar si la ciudad es valida
if (loc in set(rangos["LOCALIDAD"])): 
    location = rangos[rangos['LOCALIDAD'] == loc]
else:
    print("No se ha encontrado la localidad ingresada, Finalizando...")
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
sleep(3)
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
sleep(5)

print("\033[H\033[J", end="")

print(" -------- SQL Config Setup -------- ")

mydb = mysql.connector.connect(
  host="localhost",
  user=input("Ingrese nombre de usuario: "),
  password = input("Ingrese contraseña: ")
)

mycursor = mydb.cursor()

# --------------------
for i in range(len(numeros)):
    sql = "INSERT INTO telefono (localidad , numero) VALUES (%s, %s)"
    val = (loc, numeros[i])
    mycursor.execute(sql, val)

print("Numeros cargados correctamente, finalizando...")


