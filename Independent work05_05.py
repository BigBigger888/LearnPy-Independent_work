# Напишите программу, в которой пользователь вводит два текстовых значения, и на их основе создается новый текст.
# В этот новый текст поочередно включаются буквы из текстов, введенных пользователем. Когда один из текстов
# заканчивается, в качестве символов из этого текста используется "звездочка" *.
txt1=input("Введите первый текст: ")
txt2=input("Введите второй текст: ")
new_txt=""
if len(txt1)>len(txt2):
    k=len(txt1)-len(txt2)
    k="*"*k
    txt2=txt2+k
else:
    k=len(txt2)-len(txt1)
    k="*"*k
    txt1=txt1+k
for s in range(len(txt1)):
    new_txt+=txt1[s]
    new_txt+=txt2[s]
print("Получившийся текст", new_txt)
