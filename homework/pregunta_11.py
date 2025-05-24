"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sumas = {}
    
    with open("files/input/data.csv", 'r') as file:
        for linea in file:
            column = linea.strip().split('\t') 
            letra_col4 = column[3]
            valor_col2 = int(column[1])


            for letra in letra_col4.split(','):
                if letra in sumas:
                    sumas[letra] += valor_col2
                else:
                    sumas[letra] = valor_col2

    return dict(sorted(sumas.items()))

pregunta_11()