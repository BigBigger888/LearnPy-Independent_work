# Напишите программу, в которй на основе текста, введенного пользователем, создается новый текст. По сравнению
# с исходным в нем слова расположены в обратном порядке. Под словами подразумевать блоки текста, разделенные
# пробелами.
txt=input("Введите текст: ")
L=txt.split(" ")
M=L[::-1]
new_txt=" ".join(M)
print("Развернутый текст:",new_txt)