# Напишите программу, в которой пользователю предлагается ввести текстовое значение. На основе текста формируется
# словарь. Ключами элементов словаря являются символы из текста. Значение соответствующего элемента - это исходный
# текст, в котором "вычеркнут" тот символ, который является ключом. Если при формировании очередного элемента словаря
# окажется, что такой ключ уже есть, то соответствующий символ пропускается. Например, если пользователь ввел текст
# "ABCABD", то в словаре будут представлены элементы с ключами "A", "B", "C" и "D" со значениями соответственно
# "BCABD", "ACABD", "ABABD" и "ABCAB".
alph=input("Введите текст: ")
ind=list(alph)
A=list()
B=list()
txt=''
for z in alph:
    k=alph.index(z)
    ind.pop(k)
    for i in ind:
        txt+=i
    A.append(txt)
    B.append(z)
    ind=list(alph)
    txt=''
C=dict(zip(B,A))
print(C)

# Альтернативное решение
alph=input("Введите текст: ")
ind=list(alph)
A=list()
B=list()
for z in alph:
    k=alph.index(z)
    ind.pop(k)
    ind=''.join(ind)
    A.append(ind)
    B.append(z)
    ind=list(alph)
C=dict(zip(B,A))
print(C)