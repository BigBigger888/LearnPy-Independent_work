# Напишите программу, в которой отображаются числа из последовательности Фибоначчи. Первые два числа
# в последовательности равны единице, а каждое следующее равно сумме двух предыдущих значений
# (то есть речь о числах 1,1,2,3,5,8,13,21,34,55 и так далее). Количество чисел в последовательности
# вводится с клавиатуры
n=int(input("Введите количество чисел в последовательности: "))
if n>1:
    a=list(range(n))
    a[0]=1
    k=2
    while k!=n:
        a[k]=a[k-1]+a[k-2]
        k=k+1
    print(a)
else:
    print("Вы ввели некорректное значение, последовательность должна состоять минимум из двух чисел")