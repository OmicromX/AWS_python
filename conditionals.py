# Se va a crear un validador para saber si podemos o no entrar a una fiesta, es importante que para entrar a la fiesta debes de ser mayor de edad

# Se crea la variable edad y ella se va a guardarlo que escriba el usuario
edad = input("Escriba su edad: ")

# convertimos la variable entrada a entero debido a que cuando se escribe por consola el valor  que se guarda es el de un texto
edad = int(edad)

# Vamos a comparar si la edad es mayor o igual a 18 
if edad >= 18:
    # Imprime que lo deja entrar
    print("Puede entrar")
else:
    # Si no se cumple la condicion de ser mayor a 18 años, imprime "no se puede entrar"
    print("No puede entrar")
    
    
# Ahora se va a validar si la persona es mayor de 18 años, y además tiene más de $600
# Se crear la variable edad y en ella se guarda lo que escriba el usuario
edad = input("Escriba su edad: ")

# convertimos la variable edad a entero
edad = int(edad)

# Se crea la variable dinero y en ella se guarda lo que se escriba el usuario
dinero = input("Escriba su dinero: ")

# Convertimos la variable dinero a entero debido a que cuando se escribe por  consola el valor que se guarda es el de un texto (str)
dinero = int(dinero)

#----
if edad >= 18:
    # verificamos si cuenta con el dinero 
    if dinero >= 600:
        # Imprime que lo deja entrar
        print("Puede entrar")
    else:
        # Como no tiene el dinero no puede entrar
        print("No puede entrar")
else:
    print("No puede entrar")

# Vamos a comparar si la edad es mayor  o igual a 18 - version 2
if edad >= 18 and dinero >= 600:
    # Imprime que lo deja entrar
    print("V2 puede entrar")
else:
    # Como no tiene la edad no puede entrar
    print("V2 No puede entrar")

#------------------------------------------------------------------------------
# Condicional con la multiple comparaciones
# Creamos la variable llamada dinero

dinero = input("Escriba el dinero con el que cuenta: ")

# Convertimos la variable de str a entero
dinero = int(dinero)

if dinero<100:
    print("Le compro unas galletas")
elif dinero >=100 and dinero <=200:
    print("Le compro unos chocolates")
elif dinero >200  and dinero <=300:
    print("Le compro unas picafresas")
else:
    print("Le compro un peluche")
    

#-------------------------------------------LABORATORIO---------------------
# Creamos la variable usrRepy y en ella guardamos lo que escriba el usuario
userReply = input("Do you need to ship a package? (Enter yes or no) ")

if userReply == "yes":
    print("We can help you ship that package!")
    
else:
    print("Please come back when you need to ship a package. Thank you.")   
    
    
# En la variable userReply vamos a guardar una de estas opciones(stamps,  envelope, or copy) que deben ser escritas en la cosola,. Si no se escribe ninguna de ellas se imprime un mensaje de despedida 
    userReply = input("Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy) ")
if userReply == "stamps":
    print("We have many stamp designs to choose from.")
elif userReply == "envelope":
    print("We have many envelope sizes to choose from.")
elif userReply == "copy":
    copies = input("How many copies would you like? (Enter a number) ")
    print("Here are {} copies.".format(copies))
else:
    print("Thank you, please come again.")