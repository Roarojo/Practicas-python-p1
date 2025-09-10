




# hacer un programa que lea una cadena y que muestre en pantalla
# cuantos numeros tiene, cuantas mayusculas, cuantas minusculas 
# y cuantos espacios
def inicio():
    mi = 0
    may = 0
    c = 0
    e = 0
    numeros = "0123456789"
    cadena = input('Escribe una cadena \n')
    for i in cadena:
        if i in numeros:
            print('es numero')
            c += 1
        if ord(i) == 32:
            e += 1
        if ord(i)>=97 and ord(i)<=122:
            mi += 1
        if ord(i)>=65 and ord(i)<=90:
            may += 1
    print(f'Los numeros son: {c}\n y los espacios: {e} \n y las minusculas {mi}\n y las mayusculas {may}')

if __name__=='__main__':
    inicio()