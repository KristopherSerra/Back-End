'''
5 - Un script Python que sea capaz de crear una planilla de cálculo a modo de reporte con
los datos de una campaña publicitaria finalizada dada. Este script, además debe enviar
por mail el reporte creado al cliente en cuestión.
'''

import pandas as panda
import openpyxl

informes = panda.read_excel("C:\\Users\Kristopher\Desktop\De Todo\\Universidad\LdL\BackEnd\Laboratorio-Full-\Back-End\Informes.xlsx")

tabla_pivote = informes.pivot_table(index='Cant. Total', columns='Dia',values='Total',aggfunc='sum')
