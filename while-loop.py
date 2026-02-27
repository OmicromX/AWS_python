# Siempre que se importe una librearia debe de ir al principio del codigo
import random

# Un ciclo while es un bucle que va recorrer hasta que no se cumpla la condicion

# Se crea la variable numero y s le pide al usuario que escriba el numero 0
numero = input("Escriba el numero 0:")

# Convertimos la variable numero de str a int
numero = int(numero)

# Se verifica que lo que hay en la variable numero sea menor que 10

while numero < 10:
    # Se incrementa el valor de numero
    numero = numero+1
    # Si numero es menor que 10 se imprime su valor
    print(numero)
    
#---------------------------------------------- 
# Vamos a construir la tabla de un multiplicador de un numero
# Se crea la variable numero y se le pide al usuario que escriba el numero 0


numero = input("Escriba el numero 0:")

# Convertimos la variable numero de str a int
numero = int(numero)

# Se verifica que lo que hay en la variable numero sea menor que 10
multiplicador = 0

while numero < 10:
    # Multiplicador
    multiplicador = multiplicador + 1
    # Valor de la multiplicacion 
    multiplicacion= numero*multiplicador
    # Si numero es menor que 10 se imprime su valor 
    #print(numero,"*", multiplicador,"=", multiplicacion)
    
    print(f"{numero}*{multiplicador}={multiplicacion}")
    
    #-----------------------------LABORATOIO-------------------------------------------
# Se realizan 2 impresione
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# La libreria random genera un numero aleatorio desde un numero inicial hasta el numero final

number = random.randint(1,10)

# Se crea la variable isGuessRight y se guarda en un valo booleano(False)

isGuessRight = False

# Mientras la variable isGuessRight sea diferente de verdadero se ejecuta el codigo

while isGuessRight != True:
    # Mientras la variable isGuessRight sea diferente de verdadero se ejecuta el codigo
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        
        # Se crea la variable guess y se guara dentro de ella lo que escriba el usuario
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))