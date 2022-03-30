# Напишите программу, в которой пользователь вводит имя текстового файла, а программа отображает содержимое этого
# файла, а также создает копию этого файла с пронумерованными строками.
try:
    way=input("Введите путь до файла: ")
    A=open(way)
    txt = A.read()
    print("Содержимое файла:")
    print("***")
    print(txt)
    print("***")
    A.close()
    A=open("/Users/ilyamilochkin/PycharmProjects/LearnPy/Data.txt")
    name=input("Введите имя нового файла: ")
    print("Старт процесса копирования...")
    B=open(f"/Users/ilyamilochkin/PycharmProjects/LearnPy/{name}.txt", "xt")
    k=1
    for L in A:
        string="["+str(k)+"] "+L
        k+=1
        B.write(string)
    A.close()
    B.close()
    print("Копирование завершено!")
except FileExistsError:
    print("Ошибка: такой файл уже существует")
except:
    print("Ошибка доступа к файлу")