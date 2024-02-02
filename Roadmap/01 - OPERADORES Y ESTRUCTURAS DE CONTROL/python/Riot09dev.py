"""/*
 * EJERCICIO:
 * - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
 *   Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
 *   (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
 * - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
 *   que representen todos los tipos de estructuras de control que existan
 *   en tu lenguaje:
 *   Condicionales, iterativas, excepciones...
 * - Debes hacer print por consola del resultado de todos los ejemplos.
 *
 * DIFICULTAD EXTRA (opcional):
 * Crea un programa que imprima por consola todos los números comprendidos
 * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
 *
 * Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.
 */"""

# Operadores aritméticos
print(f"suma: 5 + 7 = {5 + 7}")
print(f"suma: 5 - 7 = {5 - 7}")
print(f"suma: 5 * 7 = {5 * 7}")
print(f"suma: 5 / 7 = {5 / 7}")
print(f"suma: 5 % 7 = {5 % 7}")
print(f"suma: 5 ** 7 = {5 ** 7}")
print(f"suma: 5 // 7 = {5 // 7}")

# Operadores de comparación
print(f"Igualdad: 10==3 es {10 == 3}")
print(f"Desigualdad: 10!=3 es {10 != 3}")
print(f"Mayor: 10 > 3 es {10 > 3}")
print(f"Menor: 10 < 3 es {10 < 3}")
print(f"Menor o Igual: 10 <= 3 es {10 <= 3}")
print(f"Mayor o igual: 10 >= 3 es {10 >= 3}")

# Operadores lógicos
print(f"AND &&: 10 + 3 == 13 and 5 - 1 == 4 es {10 + 3 == 13 and 5 - 1 == 4}")
print(f"OR ||: 10 + 3 == 14 and 5 - 1 == 4 es {10 + 3 == 14 or 5 - 1 == 4}")
print(f"NOT ||: 10 + 3 == 14  es {not 10 + 3 == 14}")

# Operadores de asignación

mi_numero = 11 #asignación
print(mi_numero) 

mi_numero += 1 # suma y asignación
print(mi_numero)

mi_numero -= 1 # resta y asignación
print(mi_numero)

mi_numero *= 2 # multi y asignación
print(mi_numero)

mi_numero /= 2 # div y asignación
print(mi_numero)

mi_numero %= 2 # modulo y asignación
print (mi_numero)

mi_numero **= 2 # exp y asignación
print(mi_numero)

# Operadores de identidad

mi_nuevo_numero = mi_numero

print(mi_nuevo_numero is mi_numero)
print(mi_nuevo_numero is not mi_numero)

# Operadores de pertenecia

print(f"r in riot is: {"r" in "riot09"}")
print(f"r not in riot is: {"r" not in "riot09"}")

#Operadores de bit
a = 10 #1010
b = 3 #0011

print(f"AND: 10 & 3 ={10 & 3}")
print(f"OR: 10 & 3 ={10 & 3}")
print(f"XOR: 10 & 3 ={10 & 3}")

"""
Estructuras de control
"""

#Condicionales

mi_string = "riot"
if mi_string == "riot":
    print("dice riot")
elif mi_string == "riot09":
    print("Es riot09")
else:
    print(" no dice riot ")

#Iterativas

for i in range(11):
    print(i)

i = 0

while i <= 10:
    print(i)
    i += 1

#manejo de exepciones

def sum_values_with_return (sum_value_1, sum_value_2):
    
    try: 
         print(sum_value_1 + sum_value_2)
    except TypeError:
        print("se produjo un error")
    #tambien se puede continuar con un else
    #un finally tambien se puede utilizar.. y se ejecuta siempre anque funcione el try o el except
    # se puede especificar los errores en este caso TypeError eso solo toma en concreto ese tipo de error si no ponemos nada toma todos los tipos
    # ademas se puede capturar con except Exeption as y una variable para almacenar o imprimir el error

my_result = sum_values_with_return (1, "2")

# extra

def extra():
# Una variable number con un rango de 1 a 56
    for number in range(10, 56):
        if number % 2 == 0 and number != 16 and number % 3 != 0:
            print(number)
            
extra()