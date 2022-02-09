# Напишите программу, в которой выполняется сортировка списка (в порядке возрастания) методом пузырька.
# Метод такой: последовательно сравниваются значения соседних элементов, и если значение элемента слева
# больше значения элемента справа, элементы меняются местами. За один полный перебор элементов в списке
# элемент с самым большим значением оказывается последним в списке. За второй перебор предпоследним
# оказывается элемент со вторым по величине значением и так далее.
from random import *
seed(2022)
num=[randint(0,100) for i in range(10)]
print(num)
k=0
while k<len(num):
    for i in range(len(num)-1):
        if num[i]>num[i+1]:
            a=num[i+1]
            num[i+1]=num[i]
            num[i]=a
    k=k+1
print(num)