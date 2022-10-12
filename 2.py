mas=[]
n=int(input('Введите размерность массива 1: '))
for i in range (n):
    i=float(input('Введите элементы массива: '))
    mas.append(i)
print(mas)
mas1=[]
n1=int(input('Введите размерность массива 2: '))
for i in range (n1):
    i=float(input('Введите элементы массива: '))
    mas1.append(i)
print(mas1)
print('Общие элементы массива 1 и массива 2: ', set(mas) & set (mas1))
