# Напишите программу с функцией, которая аргументами получает ссылку на функцию (например f()) и целое число
# (например n). Результатам является функция. которая вычисляет результат путем n-кратного применения функции f().
def fin_fun(f,n):
   if n==0:
       return
   else:
       return f(), fin_fun(f,n-1)
def fun():
    return print("fun()")
fin_fun(fun,5)