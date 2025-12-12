#Generador seguro de contraseña

#Se importa la librería secrets para que se pueda elegir caracteres aleatorios.
import secrets

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

#Se inicia un ciclo para que el usuario pueda generar varias contraseñas si así lo desea.
while True:
#Se crea una función para que cuando el usuario elija una respuesta sea solo "si" o "no" y de este modo sea más fácil el código.
    def opciones(respuesta):
        return "si" if respuesta.lower() in ("si", "s", "sí", "y") else "no"

    opcion_1 = opciones(input("¿Desea añadir mayúsculas?: "))
    opcion_2 = opciones(input("¿Desea añadir números?: "))
    opcion_3 = opciones(input("¿Desea añadir símbolos?: "))

#Si el usuario no elige ninguna opción, el programa no lo dejará avanzar.
    while opcion_1 == "no" and opcion_2 == "no" and opcion_3 == "no":

        opcion_1 = opciones(input("¿Desea añadir mayúsculas?: "))
        print("Debe elegir al menos una opción")
        opcion_2 = opciones(input("¿Desea añadir números?: "))
        opcion_3 = opciones(input("¿Desea añadir símbolos?: "))

#Se le hace saber al usuario que la contraseña será creada a partir de lo que elegió y además que se evaluará su nivel de seguridad.
    print("Generando contraseña aleatoria...")
    print("Evaluando nivel de seguridad...")

#Se crea una variable para almacenar la contraseña que se va a generar. Por defecto, es en minúsculas.
    contraseña = letras_minusculas

#Dependiendo de las opciones que elija el usuario, se irán añadiendo los caracteres a la variable de la contraseña.
    if opcion_1 == "si":
        contraseña += letras_mayusculas
    if opcion_2 == "si":
        contraseña += numeros
    if opcion_3 == "si":
        contraseña += simbolos

#Se genera la contraseña con la longitud y los caracteres elegidos por el usuario.
    resultado = ''.join(secrets.choice(contraseña) for i in range(longitud))

#Se evalua la contraseña y se le indica al usuario si es segura o débil.
#Para esto se crea la variable puntos, que se incrementará en cada una de las opciones elegidas, iniciando por la longitud.
    puntos = 0

    if longitud >= 10:
        puntos += 7

    elif longitud >= 6:
        puntos += 5
    elif longitud >= 4:
        puntos += 3
    else:
        puntos += 1

#Las opciones elegidas por el usuario también incrementan los puntos.
    if opcion_1 == "si":
        puntos += 1

    if opcion_2 == "si":
        puntos += 1

    if opcion_3 == "si":
        puntos += 1

#Dependiendo de los puntos obtenidos, se le asigna un nivel de seguridad a la contraseña.
    nivel_de_seguridad = ""
    if puntos >= 10:
        nivel_de_seguridad = "Segura"
    elif puntos >= 7:
        nivel_de_seguridad = "Media"
    elif puntos >= 4:
        nivel_de_seguridad = "Débil" 
    else:
        nivel_de_seguridad = "Muy débil"

#Se le muestra al usuario la contraseña generada y su nivel de seguridad.
    print("Contraseña generada: " + resultado)
    print("Nivel de seguridad: " + nivel_de_seguridad)

#Se le pregunta al usuario si desea generar otra contraseña.
    def opciones(respuesta):
        return "si" if respuesta.lower() in ("si", "s", "sí", "y") else "no"

    continuar = opciones(input("¿Desea generar otra contraseña?: "))

    if continuar == "si":
        continue
    else:
        break
