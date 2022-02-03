# Напишите программу, в которой создается два списка одинакового размера. На основе этих списков поочередной
# вставкой элементов из первого и второго списка формируется новый список.
from random import *
seed(2022)
m=int(input("Введите размер списков: "))
a=[randint(1,100) for i in range(m)]
b=[randint(1,100) for i in range(m)]
print(a)
print(b)
num=list()
for i in range(len(a)):
    num.append(a[i])
    num.append(b[i])
print(num)