import csv
import os 

#definir rutas
ruta_relativa = "csv_vacio.scv"
ruta_absoluta = "/Users/oscarrodriguez/Documents/PYTHON COURSE ADVENCE/05_ARCHIVOS_CSV/csv_vacio.csv"
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)

"""
archivo_abierto = open(ruta_relativa, "w")
writer = csv.writer(archivo_abierto, delimiter=",")
archivo_abierto.close()
"""