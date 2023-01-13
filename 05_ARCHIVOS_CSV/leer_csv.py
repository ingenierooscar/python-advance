import csv

with open("datos.csv", "r", encoding="UTF-8") as archivo:
     readerDic = csv.DictReader(archivo)
     for filas in readerDic:
         print(filas)   

    



"""""
leer en forma de lista
reader = csv.reader(archivo)

linea_saltada = next(archivo)
print("linea saltada:", linea_saltada)

for fila in reader:
  print(fila)
   print(fila[0])"""
