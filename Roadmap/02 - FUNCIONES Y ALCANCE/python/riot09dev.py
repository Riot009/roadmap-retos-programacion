
"""/*
 * EJERCICIO:
 * - Crea ejemplos de funciones básicas que representen las diferentes
 *   posibilidades del lenguaje:
 *   Sin parámetros ni retorno, con uno o varios parámetros, con retorno...
 * - Comprueba si puedes crear funciones dentro de funciones.
 * - Utiliza algún ejemplo de funciones ya creadas en el lenguaje.
 * - Pon a prueba el concepto de variable LOCAL y GLOBAL.
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *   (y tener en cuenta que cada lenguaje puede poseer más o menos posibilidades)
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea una función que reciba dos parámetros de tipo cadena de texto y retorne un número.
 * - La función imprime todos los números del 1 al 100. Teniendo en cuenta que:
 *   - Si el número es múltiplo de 3, muestra la cadena de texto del primer parámetro.
 *   - Si el número es múltiplo de 5, muestra la cadena de texto del segundo parámetro.
 *   - Si el número es múltiplo de 3 y de 5, muestra las dos cadenas de texto concatenadas.
 *   - La función retorna el número de veces que se ha impreso el número en lugar de los textos.
 *
 * Presta especial atención a la sintaxis que debes utilizar en cada uno de los casos.
 * Cada lenguaje sigue una convenciones que debes de respetar para que el código se entienda.
 */"""

# Simples

def greet():
    print("hola mundo")

greet()

# Con retorno

def return_greet():
    return "hola mundo"

print(return_greet())

# Con argumento

def arg_greet(name):
    print(f"hola, {name}")

arg_greet("mundo")


def args_greet(greet,name):
    print(f"{greet}, {name}!")

args_greet("hola", "mundo")

# Con argumentos predeterminados

def default_arg_greet(name="mundo"):
    print(f"hola, {name}")

default_arg_greet()
default_arg_greet("python")

# Con argumentos y retorno

def return_args_greet(greet, name):
    return f"{greet}, {name}!"

print(return_args_greet("Hi", "Riot09dev"))

# Con retorno de varios valores

def muliple_return_greet():
    return "Hola", "Python"

greet, name = muliple_return_greet()
print(greet)
print(name)

# Con unnumero variable de argumentos

def variable_arg_greet(*names):
    for name in names:
        print(f"Hola, {name}!")

variable_arg_greet("Python","Riot","Diego","Riot09dev")

# Con un numero variable de argumentos con palabras clave

def variable_key_arg_greet(**names):
    for key, value in names.items():
        print(f"Hola, {key}, ({value})!")

variable_key_arg_greet(
    language="Python",
    name="Diego",
    alias="Riot",
    age="32"
)

# Funciones dentro de funciones

def otra_funcion():
    def inner_function():
        print("Hola, Python")
    inner_function()

# Funciones propias del lenguaje (built in)


otra_funcion()

print(len("Riot09"))
print(type(9))
print("Riot09".upper())
print("Riot09".lower())

#variables locales y globales

global_variable = "Python"

def hello_python():
    local_var = "Riot09"
    print(f"Hola, {global_variable}")

hello_python()
# print(local_var)



# Extra

def imprimir_numeros_y_contar(texto1, texto2):
    # Inicializamos un contador para llevar la cuenta de las veces que se imprime un número
    contador = 0

    # Iteramos sobre los números del 1 al 100
    for numero in range(1, 101):
        # Verificamos si el número es múltiplo de 3 y 5 al mismo tiempo
        if numero % 3 == 0 and numero % 5 == 0:
            print(f"{texto1}{texto2}")
        # Si no es múltiplo de 3 y 5, verificamos si es múltiplo de 3
        elif numero % 3 == 0:
            print(texto1)
        # Si no es múltiplo de 3, verificamos si es múltiplo de 5
        elif numero % 5 == 0:
            print(texto2)
        # Si no es múltiplo de 3 ni de 5, simplemente imprimimos el número
        else:
            print(numero)

        # Incrementamos el contador cada vez que se imprime algo
        contador += 1

    # Retornamos el valor del contador al final de la función
    return contador

# Ejemplo de uso:
texto1 = "Fizz"
texto2 = "Buzz"
# Llamamos a la función con los textos proporcionados
veces_impreso = imprimir_numeros_y_contar(texto1, texto2)

# Imprimimos la cantidad de veces que se ha impreso un número
print(f"La función ha impreso números {veces_impreso} veces.")
