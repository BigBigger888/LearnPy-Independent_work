# Напишите программу, в которой шифруется и дешифруется введенный пользователем текст. При шифровании каждая буква
# заменяется на следующую (а последняя - на первую), но только эта операция выполняется для гласных букв и для
# согласных. Для этого нужно сформировать список гласных и согласных букв и шифрование и дешифрование выполнять
# на основе этих списков.
# Формирование списков гласных и согласных букв
n=ord("а")
m=ord("я")
alph=list()
for s in range(ord("я")-ord("а")+1): # формирование списка - алфавит от а до я
    alph.append(chr(n+s))
glass_list=["а", "е", "и", "о", "у", "ы", "э", "ю", "я"] # список согласных букв
sogl_list=list()
v=0
for s in alph: # создание списка гласных букв на основе списка-алфавита
    for k in glass_list:
        if s!=k:
            v+=1
        if v==9:
            sogl_list.append(s)
    v=0
# Формирование списков больших гласных и согласных букв
N=ord("А")
M=ord("Я")
alph_big=list()
for s in range(ord("Я")-ord("А")+1): # формирование списка - алфавит болших букв от а до я
    alph_big.append(chr(N+s))
glass_list_big=["А", "Е", "И", "О", "У", "Ы", "Э", "Ю", "Я"] # список согласных больших букв
sogl_list_big=list()
v=0
for s in alph_big: # создание списка больших  гласных букв на основе списка-алфавита больших букв
    for k in glass_list_big:
        if s!=k:
            v+=1
        if v==9:
            sogl_list_big.append(s)
    v=0
# Основная часть пограммы
# Шифрование
txt=input("Введите текст для шифрования: ")
new_txt=""
new_txt_big=""
new_txt_fin=""
new_txt_fin_big=""
for s in txt:
    for i in range(len(glass_list)):
        if s=="я":
            s="а"
            break
        elif s==glass_list[i]:
            s=glass_list[i+1]
            break
    new_txt+=s
for s in new_txt:
    for i in range(len(glass_list_big)):
        if s=="Я":
            s="А"
            break
        elif s==glass_list_big[i]:
            s=glass_list_big[i+1]
            break
    new_txt_big+=s
for s in new_txt_big:
    for i in range(len(sogl_list)):
        if s=="ь":
            s="б"
            break
        elif s==sogl_list[i]:
            s=sogl_list[i+1]
            break
    new_txt_fin+=s
for s in new_txt_fin:
    for i in range(len(sogl_list_big)):
        if s=="Ь":
            s="Б"
            break
        elif s==sogl_list_big[i]:
            s=sogl_list_big[i+1]
            break
    new_txt_fin_big+=s
print("Шифр:",new_txt_fin_big)
# Дешифрование
new_txt_def=""
new_txt_def_big=""
new_txt_fin_def=""
new_txt_fin_def_big=""
for s in new_txt_fin_big:
    for i in range(len(glass_list)):
        if s=="а":
            s="я"
            break
        elif s==glass_list[i]:
            s=glass_list[i-1]
            break
    new_txt_def+=s
for s in new_txt_def:
    for i in range(len(glass_list_big)):
        if s=="А":
            s="Я"
            break
        elif s==glass_list_big[i]:
            s=glass_list_big[i-1]
            break
    new_txt_def_big+=s
for s in new_txt_def_big:
    for i in range(len(sogl_list)):
        if s=="б":
            s="ь"
            break
        elif s==sogl_list[i]:
            s=sogl_list[i-1]
            break
    new_txt_fin_def+=s
for s in new_txt_fin_def:
    for i in range(len(sogl_list_big)):
        if s=="Б":
            s="Ь"
            break
        elif s==sogl_list_big[i]:
            s=sogl_list_big[i-1]
            break
    new_txt_fin_def_big+=s
print("Дешифрованное сообщение:",new_txt_fin_def_big)