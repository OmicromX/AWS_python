# Se crea la lista myMixedTypeList en la cual se crea diferentes tipos de datos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# El cilo for se encarga de mirar cada uno de los elemtentos de la lista

for item in myMixedTypeList:
    # En esta impresion se van a mostrar cada uno de los elementos de la lista, primero seu valor y luego el tipo de datos
    print("{} is of the data type {}".format(item,type(item)))