def inicio():
    c =0
    while True:
        n=input('Escribe un nombre')
        e=input('Escribe una edad')
        g=input('Esribe el genero')
        aux = 'nombre: ' + n + 'edad: ' + e + 'genero: ' + g
        lis1.append(n)
        lis1.append(e)
        lis1.append(g)
        lis2.append(lis1)
        lis1.pop(0)
        c+=1
        if c >=5:
            break
    print(lis2)

lis1=[]
lis2 = []
if __name__=='__main__':
    inicio()

# personas = []
# for i in range(5):
#     print(f"\nDatos de la persona{i+1}:")

#     nombre = input ("ingresa un nombre")
#     edad = int(input("ingresa una edad"))
#     sexo = input ("ingresa el sexo (M/F)").upper()

#     persona ={
#         "nombre": nombre,
#         "edad": edad, 
#         "sexo": sexo 
#     }
#     personas.append(persona)

# print("\nDatos de todas las personas:")
# for persona in personas:
#     print(f"nombre:{persona['nombre']},{persona['edad']}, sexo: {persona['sexo']}")