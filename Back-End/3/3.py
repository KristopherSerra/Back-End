import openpyxl

book = openpyxl.load_workbook('rangos.xlsx', data_only=True)
sheet = book["rangos"]
indicativo = []

localidad = input("Ingrese localidad:")


for rows in sheet.iter_cols(min_col = 1, max_col = 1, min_row = 2, max_row = 115):
    for row in rows:
        if (row.value == localidad):
            print(row.value)
        