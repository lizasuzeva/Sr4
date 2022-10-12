mas=[]
n=int(input('Введите размерность массива '))
for i in range (n):
    i=float(input('Введите элементы массива: '))
    mas.append(i)
print(mas)
element=max(mas)
print('Наибольший элемент массива:',element)
start = mas.index(max(mas)) + 1
mas[start:] = [0] * (len(mas) - start)
print(mas)
