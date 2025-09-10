# # instrucciones de entrada y salida
# # print() o print(f)
# print('Hola mundo')
# print(f'Hola mundo numeros {10}')
# # Entrada datos
# input('Escribe un numero') #se introducen solo letras
# #casting para convertir a valores especificos
# f = 0.0
# f = float(input('Escribe un numero con decimales'))
# a = 0
# a = int(input('Escribe un numero'))
# c = 120
# print(str(c))
# v = ""
# v = str(c)
# #Nota: solo las variables que no se introducen por teclado se obliga a inicializarlas.

#hacer un programa que lea nombre y precio de un producto, el programa calculara
#el el costo y precio de venta.
# costo involucra el 12% y iva 16%

for i in range(0,5):# rango valor inicial hasta valor final sin incluirlo
    precio = 12.55
    nombre = input('Escribe un nombre de un producto')
    precio = float(input('Escribe el precio del producto'))
    costo = precio * 1.12
    precioventa = costo * 1.16
    print(f'el costo es {costo:.2f} y el precio de venta {precioventa:.2f}')
    print(f'el costo es {costo} y el precio de venta {precioventa}')0
    #res = input('Deseas otro numero (s/n) \n')
    # if res == 'n' or res == 'N':
    #     break




