# Напишите программу, которая выполняется следующим образом. Пользователь вводит целое неотрицательное число.
# На основе этого числа создается список из натуральных чисел от 1 до этого числа. Затем на основе этого списка
# создается словарь. Элементы списка служат ключами для элементов словаря. Значения элементов словаря определяются
# на основе значений элементов списка, но взятых в обратном порядке. Например, если пользователь вводит число 3,
# то создается список [1,2,3] и на его основе создается словарь из трех элементов. У элемента с ключом 1 значение 3,
# у элемента с ключом 2 значение 2, а у элемента с ключом 3 значение 1.
n=int(input("Введите целое неотрицательное число: "))
num=list(range(1,n+1)) # список натуральных чисел от 1 до n
vac={k: num[-k] for k in num}
print(vac)
