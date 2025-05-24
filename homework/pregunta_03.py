"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    fila = []
    with open("files/input/data.csv", "r", encoding="utf-8") as f:
        for line in f:
            renglon = list(line.strip().split("\t"))
            letra = renglon[0]
            numero = int(renglon[1])
            fila.append((letra, numero))
    secuence = sorted(fila)
    dicc = {}
    for key, value in secuence:
        if key in dicc:
            dicc[key] += value
        else:
            dicc[key] = value
    return list(dicc.items())

pregunta_03()