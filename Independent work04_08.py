# Напишите программу, в которй используется словарь. Ключами в словаре являются фамилии писателей, а значение
# соответствующего элемента - название произведения, написанного автором. В программе перебираются значения всех
# элементов словаря, и для каждого значения (название произведения) пользователю предлагается указать фамилию автора.
# После перебора содержимого словаря и получения всех ответов программа отображает количество правильных ответов
# пользователя.
A=dict(Толстой='Война и Мир',Достоевский='Преступление и наказание',Чехов='Толстый и тонкий')
k=0
print("Введите фамилии авторов напротив названий произведений:")
for z in A:
    B=input(A[z]+' ')
    if B in A:
        k=k+1
print("Количество правильных ответов:", k,"из", len(A))