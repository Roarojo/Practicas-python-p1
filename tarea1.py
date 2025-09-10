arr = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
car = []
c = 0
c2 = 0
while(True):
    a = input('Escribe un datos o valor \n')
    if a.isdigit():
        arr[c] = int(a)
    elif a.isalpha():
        car.append(a)
    c += 1
    if c >=10:
        break
print(f'la lista tiene {len(car)}')
for i in arr:
    if i != -1:
        c2 += 1
print(f'el arreglo tiene {c2}')
print(car)
print(arr)




