# Напишите программу, которая на основе списка из натуральных чисел формирует целое число.
# Число формируется "объединением" элементов списка: например, если исходный список [12,3,456,78],
# то программа должна получить число 12345678.
n=int(input("Введите значение 'n': "))
num=[12,3,456,78]#list(range(n))
for s in num:
    print(s, end="")
