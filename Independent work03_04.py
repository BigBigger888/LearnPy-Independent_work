# Напишите программу, в котрой есть функция для заполнения вложенного списка. Список заполняется натуральными числами
# "змейкой": сначала заполняется первая строка, затем последний столбец (сверху вниз), последняя строка (справа налево),
# первый столбец (снизу вверх), вторая строка (слева направо), и так далее.
def show(A):
    for a in A:
        for s in a:
            print(s, end=" ")
        print()
def num(m,n):
    a=0
    k=1
    s=0
    z=0
    num=[["1" for j in range(n)]for i in range(m)]
    while s<m:
        for i in range(k):
            for j in range(s,n-s):
                num[i+s][j]=a
                a=a+1
        for i in range(k+s,m-s):
            num[i][-1-s]=a
            a=a+1
        for i in range(m-1-s,m-s):
            for j in range(1+s,n-s):
                num[i][-j-1]=a
                a=a+1
        for i in range(k+1,m-z-s):
            num[-i-s][0+s]=a
            a=a+1
        s=s+1
        z=z+1
    return num
m,n=eval(input("Введите размерность вложенного списка: "))
show(num(m,n))
