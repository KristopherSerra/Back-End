import openpyxl

# Abrir archivo (en este caso carga el archivo de los rangos)
book = openpyxl.load_workbook('Rangos.xls', data_only=True)


# Seleccion de la hoja ------------------
sheet = book["bde"]


# Seleccion de area ----------------------
celdas = sheet['A2' : 'D6']  #


localidad = input("Ingrese localidad")




# Lista para almacenar los datos ---------
rango = []  

'''
print ("Bienvenido")
print("Ingrese el Operador de telofono que utiliza:")
operador = input(str())
print("Ingrese el Tipo de Servicio:")
servicio = input(int())
print("Ingrese la Modalidad de Servicio:")
modalidad = input(str())
print("Ingrese la Localidad del Numero Telefonico:")
localidad = input(str())
print("Ingrese el Indicativo del Numero Telefonico:")
indicativo = input(int())
print("Ingrese el Bloque de la Localidad del Numero Telefonico:")
bloque = input(int())
print("Ingrese la Fecha:")
fecha = input(date())
'''