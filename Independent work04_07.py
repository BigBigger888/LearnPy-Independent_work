# Напишите программу, которая выполняется следующим образом. Пользователь вводит текст. На основе этого текста
# создается словарь. Ключами словаря служат символы из текста, а значениями элементов словаря являются количества
# вхождений соответствующих символов в текст. Например, если пользователь воодит текст "ABBCAB", то словарь будет
# состоять из трех элементов с ключами "A", "B" и "C", а значения элементов соответственно равны 2
# (в тексте 2 буквы "A"), 3 (в тексте 3 буквы "B") и 1 (в тексте 1 буква "C").
alph=input("Введите текст: ")
A={z: alph.count(z) for z in alph if z==z}
print(A)