# La libreria csv nos perimite trabajar con archivos separados por coma
import csv

# La libreria copy nos permite tomar datos de un archivo y usarlos dentro de un porgrama
import copy

# Se crea el diccionario MyVehicle
myVehicle = {
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

# Se crea un ciclo for para imprime cada una de las clave:valor que hay dentro del diccionario
for key, value in myVehicle.items():
    print("{} : {}".format(key,value))
    
# Se crea una lista vacia
myInventoryList = []

# Se abre el archivo
with open('car_fleet.csv') as csvFile:
    # Se lee el archivo de csvReader donde su delimitador son las ,
    csvReader = csv.reader(csvFile, delimiter=',')  
    
    # Se crea la variable lineCount y se asigna el valor d 0
    lineCount = 0  
    
    # Se lee cada una de la lineas es 0
    for row in csvReader:
        if lineCount == 0:
            # Se imprime el nombre de la columna 
            print(f'Column names are: {", ".join(row)}')  
            # S aumenta en 1 el valor de lineCount
            lineCount += 1  
            
        # Si el valor de la lineas ni es 0    
        else:  
            # Se imprime el nombre de la columna
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)  
            currentVehicle["vin"] = row[0]  
            currentVehicle["make"] = row[1]  
            currentVehicle["model"] = row[2]  
            currentVehicle["year"] = row[3]  
            currentVehicle["range"] = row[4]  
            currentVehicle["topSpeed"] = row[5]  
            currentVehicle["zeroSixty"] = row[6]  
            currentVehicle["mileage"] = row[7]  
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("-----")
    
