# Напишите программу, в которой создается текстовый файл. Имя файла вводится пользователем. Текст для файла вводится
# пользователем. При записи текста в файл, все маленькие буквы заменяются на большие.
try:
    print("Создание нового файла...")
    name=input("Введите имя нового файла: ")
    A=open(f"/Users/ilyamilochkin/PycharmProjects/LearnPy/{name}.txt", "xt")
    txt=input("Введите текст для записи в файл: ")
    A.write(txt.upper())
    print("Новый файл создан!")
except FileExistsError:
    print("Ошибка: такой файл уже существует")
except:
    print("Ошибка доступа к файлу")