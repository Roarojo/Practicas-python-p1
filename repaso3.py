
# def validar(a):
#     c = 0
#     d = 0.0
#     try:
#         c = int(a)
#         print('Es un valor numerico sin decimales')
#     except ValueError:
#         print('No es un valor numerico sin decimales')
    
#     try:
#         d = float(a)
#         print('Es un valor numerico con decimales')
#     except ValueError:
#         print('No es un valor numerico con decimales')


# def leer():
#     # ord que obtiene el ascii del caracter
#     # isalpha para caracteres
#     # isdigit para numeros
#     #try  except ValueError: 
#     a = input('Escribe un dato o valor')
#     validar(a)

def validar(a):
    ne = 0
    nf = 0.0
    try:
        ne = int(a)
        return ne
    except ValueError:
        print('No es un entero')
    try:
        nf = float(a)
        return nf
    except ValueError:
        print('No es un numero con decimales')
    return a

def leer():
    a = input('Escribe un dato \n')
    dato =validar(a)
    lista.append(dato)


lista = []
if __name__ == '__main__':
    while(True):
        leer()
        res = input('Deseas otro s/n')
        if res == 'n' or res == 'N':
            print(lista)
            break