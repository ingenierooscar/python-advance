def calcualar_area_cuadrado(lado):
    area = lado*lado
    return area



lado_cuadrados = [1,2,3]
area_cuadrados = []
for lado in lado_cuadrados:
    area = calcualar_area_cuadrado(lado)
    area_cuadrados.append(area)   