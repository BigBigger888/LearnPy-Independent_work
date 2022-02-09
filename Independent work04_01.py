# Напишите программу, в которой генерируется 15 случайных целых чисел: 5 чисел попадают в диапазон значений
# от 1 до 10 и 10 чисел попадают в диапазон от 10 до 30.
from random import *
seed(2022)
num=set()
A=set()
B=set()
while len(A)<5:
    A.add(randint(1,10))
while len(B)<10:
    B.add(randint(10,30))
num=list(A)+list(B)
for s in num:
    print(s, end=" ")
