# Напишите программу, в которой пользователь вводит два действительных числа, а программа проверяет,
# какое из чисел больше. Используйте тернарный оператор и обработку исключительных ситуаций.
try:
    a, b = eval(input("Введите два действительных числа: "))
    if a==b:
        print(a, "=", b)
    else:
        c=a if (int(a)>int(b)) else b
        if c==a:
            print(c, ">", b)
        else:
            print(c,">", a)
except:
    print("Вы ввели некорректные данные.")
print("Выполнение программы завершено!")