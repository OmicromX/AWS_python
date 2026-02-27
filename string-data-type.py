#Creamos una variable myString y dentrp de ella se guarda el texto "This is a string"
myString = "This is a string."

#Imprimimos el valor el valor de la variable string
print(myString)

# Imprimimos el tipo de dato de la variable mystring
print(type(myString))

# Imprimimos el valor de la variablemyString, un texto y finalete el tipo de dato de la variable myString
print(myString + " is of the data type " + str(type(myString)))


# Creamos la variable firstString y dentro de ella guardamos el valor de "Water"
firstString = "water"

# Creamos la variable de secondString y dentro de ella guardamos el valor de "fall"
secondString = "fall"

# Creamos la variable de thirdString y dentro de ella guardamos el valor de concatenado (unido) de las variables firtString y secondString

thirdString = firstString + secondString

# Imprimimos el valro de la variable thirString
print(thirdString)

# Creamos la Variable name y usando la funcion input() vamos a almacenar lo que escriba el usuario por consola
name = input("What is your name?")

# Imprimimos el valor de la variable name
print(name)

# Creamos la variable color y usando la funcion input() vamos a almacenar lo que escriba el usario por consola
color = input("What is your favorite color?  ")

# Creamos la variable favorite animal y usando la funcion input() vamos a almacenar lo que escriba el usario por consola

animal = input("What is your favorite animal?  ")

#  Para imprimir usando  format() vamos a poner un {} por cada variable  y el format {} va a poner el valor de las variables en el orden que se est[a usando]

print("{}, you like a {} {}!".format(name,color,animal))
