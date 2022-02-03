# Напишите программму, в которой создается числовой список. Список заполняется случайными числами. Затем
# элементы с четными индексами сортируются в порядке возрастания, а элементы с нечетными индексами
# сортируются в порядке убывания.
from random import *
seed(2022)
num=[randint(1,100) for i in range(10)]
print(num)
a=[]
b=[]
for i in range(len(num)):
    if i%2!=0:
        a.append(num[i])
        a.append(num[i])
        a=sorted(a,reverse=True)
    else:
        b.append(num[i])
        b.append(num[i])
        b=sorted(b)
num=[b[i] if i%2==0 else a[i] for i in range(len(num))]
print(num)
