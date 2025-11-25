#Generador seguro de contraseña

#Se crean las variables con los caracteres que se van a utilizar al momento de generar la contraseña segura.

letras_minusculas = "abcdefghijklmnñopqrstuvwxyz" 
letras_mayusculas = letras_minusculas.upper()
numeros = "0123456789"
simbolos = "@!*#$%"

#Se pregunta al usuario la longitud de caracteres que desea en la contraseña.

longitud = input("Ingresa la longitud deseada para la contraseña: ")

#Si el usuario escribe palabras, el programa no lo dejará avanzar hasta que escriba un número.
while not longitud.isdigit():     
    print("Debe ingresar solo números, no letras")
    longitud = input("Ingresa la longitud deseada para la contraseña: ")

#La cadena de texto se hace número y se le hace saber al usuario que es válida la longitud.
longitud = int(longitud) 
print("Longitud válida")


#Se crea una función para que cuando el usuario elija una respuesta sea solo "si" o "no" y de este modo sea más fácil el código.
def opciones(respuesta):
    return "si" if respuesta.lower() in ("si", "s", "sí", "y") else "no"

opcion_1 = opciones(input("¿Desea añadir mayúsculas?: "))
opcion_2 = opciones(input("¿Desea añadir números?: "))
opcion_3 = opciones(input("¿Desea añadir símbolos?: "))

#Si el usuario no elige ninguna opción, el programa no lo dejará avanzar.
while opcion_1 == "no" and opcion_2 == "no" and opcion_3 == "no":

    print("Debe elegir al menos una opción")
    opcion_1 = opciones(input("¿Desea añadir mayúsculas?: "))
    opcion_2 = opciones(input("¿Desea añadir números?: "))
    opcion_3 = opciones(input("¿Desea añadir símbolos?: "))

#Se le hace saber al usuario que la contraseña será creada a partir de lo que elegió y además que se evaluará su nivel de seguridad.
print("Generando contraseña aleatoria...")
print("Evaluando nivel de seguridad...")

