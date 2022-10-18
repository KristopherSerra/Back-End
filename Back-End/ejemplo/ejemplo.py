import openpyxl

#https://www.youtube.com/watch?v=1xjgY5Wpwto
#https://www.youtube.com/watch?v=WMPZMeAQX3Q

# Abrir archivo (en este caso carga uno existente)
book = openpyxl.load_workbook('test.xlsx', data_only=True)



# Seleccion de la hoja ------------------
sheet = book.active



# Escritura en el archivo ----------------
#sheet['A1'] = 10
#sheet['A2'] = 15



# Guardar --------------------------------
#book.save('numbers.xlsx')



# Seleccion de area ----------------------
celdas = sheet['A2' : 'D6']



# Lista para almacenar los datos ---------
personas =[]  



# Imprimir todas las celdas --------------
#for fila in celdas: 
#    print([celda.value for celda in fila])



#Guardar en la lista ---------------------
for fila in celdas: 
    persona = ([celda.value for celda in fila])
    personas.append(persona)


# Imprimir personas ----------------------
#for persona in personas:
#    print(f"{persona[0]} tiene {persona[1]} anios")



# Guardar celda en variable --------------
nombre = sheet['A2'].value

print(nombre)


