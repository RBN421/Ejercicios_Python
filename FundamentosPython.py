def nuevoTema(tema):
    print("\n---------- ",tema," ----------\n")

nuevoTema("Operadores Aritméticos")
print("Operador Suma, 5 + 3 = ",5 + 3)
print("Operador Resta, 10 - 2 =", 10 - 2)
print("Operador Multiplicación, 3 * 3 =", 3 * 3)
print("Operador División, 20 / 3 =", 20 / 3)
print("Operador División Entera, 20 // 3 =", 20 // 3)
print("Operador Modulo, 20 % 3 =", 20 % 3)
print("Operador Cambio de Signo, -3 =", -3)
print("Operador Exponente, 5 ** 5 =", 5 ** 5)

#Este es un comentario de una línea.
'''Este es un omnetario
de varias lineas'''
nuevoTema("Operadores Lógicos")
# Actividad: Imprmir la tabla de verdad del and
print("True and True: ", True and True) #Operador Lógico and.
print("True and False: ", True and False)
print("False and True: ", False and True)
print("False and False: ", False and False)
# Actividad: Imprmir la tabla de verdad del or
print("\nTrue or True: ", True or True) #Operador Lógico or.
print("True or False: ", True or False)
print("False or True: ", False or True)
print("False or False: ", False or False)
# Actividad: Imprmir la tabla de verdad del not
print("\nnot True: ", not True) #Operador Lógico not.
print("not False: ", not False)

nuevoTema("Operadores de Comparación")
print("3 == 3: ", 3 == 3)
print("5 != 4: ", 5 != 9)
print("5 < 3: ", 5 < 3)
print("3 > 5: ", 3 > 5)
print("4 <= 8: ", 4 <= 8)
print("5 >= 3: ", 5 >= 3)

nuevoTema("Variables")
variable1 = 10
_variable2 = 6.2547
variable3 = "Pepe"
nombreVariable = 8
nombre_variable = 34.2
print(variable1, _variable2, variable3, nombreVariable, nombre_variable)
a, b, c = 5, 10.8, "Hola"
print(a)
print(b)
print(c)

nuevoTema("Enteros")
w = 105
x = 1234567898745
y = -58
z = 0b00110011
h = 0xff
print(w, type(w))
print(x, type(x))
print(y, type(y))
print(z, type(z))
print(h, type(h))

nuevoTema("Flotantes")
x = 1234.56
print(x, type(x))
y = -9874.56
print(y, type(y))

nuevoTema("Numeros Complejos")
x = -46j
y = 12 + 45j
z = 2j
print(x, type(x))
print(y, type(y))
print(z, type(z))

nuevoTema("Booleanos")
lis = []
print(lis, 'is', bool(lis))
t = ()
print(t, 'is', bool(t))
new = 'Hello'
print(new, 'is', bool(new))
num = 99
print(num, 'is', bool(num))
comp = 0+0j
print(comp, 'is', bool(comp))
val = None
print(val, 'is', bool(val))

nuevoTema("Listas")
a = [10, 20.5, "Python List"]
print(a)
print(a[0])
print(a[1])
print(a[2])

nuevoTema("Tuplas")
t = (25, 'Tuple', 1+10j)
print(t)
print("t[1] = ", t[1])
print("t[0:3] = ", t[0:3])

nuevoTema("Cadenas")
s = "Esta es una cadena de una linea"
s2 = 'Esta tambien es una cadena de una linea'
s3 = '''Una cadena
Multilinea  con tabulares
y saltos de
linea'''
print(s, type(s))
print(s2, type(s2))
print(s3, type(s3))
s4 = "Hola" * 4
print(s4)

nuevoTema("Conjuntos (Sets)")
a = {50,20,30,10,40}
print("a = ", a)
print(type(a))

nuevoTema("Diccionarios")
d = {1:'val',2:'val2'}
print(type(d))
print("d[nom] = ", d[1])
print("d[num] = ", d[2])
datos = {"Nombre": "Rodolfo", "Edad": "40", "Tel": "0123456789"}
print(datos)
print(datos["Nombre"])
print(datos["Edad"])
print(datos["Tel"])