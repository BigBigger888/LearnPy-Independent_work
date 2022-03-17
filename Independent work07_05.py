# Напишите программу, в которой пользователь вводит две рациональные дроби, а программа вычисляет сумму,
# произведение, разность и частное этих дробей, среди полученных значений находит наибольшее и наименьшее и
# отображает результат вычислений.
from fractions import Fraction
def indrob(a,b):
    A=Fraction(a,b)
    return A
che=list()
try:
    num1=input("Введите первую дробь в формате A/B: ")
    num1_ev=num1.partition('/')
    first=indrob(eval(num1_ev[0]),eval(num1_ev[2]))
    num2=input("Введите вторую дробь в формате A/B: ")
    num2_ev=num2.partition('/')
    second=indrob(eval(num2_ev[0]),eval(num2_ev[2]))
    A=first+second
    B=first*second
    if first>=second:
        C=first-second
        D=first/second
    else:
        C=second-first
        D=second/first
    che.append(A)
    che.append(B)
    che.append(C)
    che.append(D)
    Ma = max(che)
    Mi = min(che)
    print(f"Сумма дробей: {che[0]}")
    print(f"Произведение дробей: {che[1]}")
    print(f"Разность дробей: {che[2]}")
    print(f"Частное дробей: {che[3]}")
    print(f"Наибольшее среди полученных значений - {Ma}, наименьшее - {Mi}.")
except ZeroDivisionError:
    print("Знаменатель дроби не должен быть равен нулю.")
except NameError:
    print("Числитель и знаменатель дроби должны быть числами.")