'''
5 - Un script Python que sea capaz de crear una planilla de cálculo a modo de reporte con
los datos de una campaña publicitaria finalizada dada. Este script, además debe enviar
por mail el reporte creado al cliente en cuestión.
'''

import pandas as pd
import openpyxl

informes = pd.read_excel("5\BDE.xlsx")
tabla_pivote = informes.pivot_table(index="LOCALIDAD",columns='BLOQUE', values='INDICATIVO', aggfunc='sum').round(0)
tabla_pivote.to_excel('5\InformeAutomatico.xlsx', startrow=4,starcolumn=2,sheet_name='Octubre 2022')