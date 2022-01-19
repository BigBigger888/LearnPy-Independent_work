# Напишите программу, в которой сравниваются (на предмет равенства) два числовых списка.
# Два списка равны, если они одинакового размера и у них соответствующие элементы.
a=[1,2,3,4,5,6,7,8,9]
b=[1,2,3,4,5,6,7,8,9]
print(a)
print(b)
la=len(a)
lb=len(b)
print(la,lb)
if la==lb:
    k=0
    while k<=la-1:
        if a[k]==b[k]:
            k+=1
        else:
            print("Списки не равны")
            raise SystemExit(0)
else:
    print("Списки не равны")
print("Списки равны")

#Альтернативное решение
atxt,btxt="",""
for s in a:
    txt=str(s)
    atxt+=txt
for s in b:
    txt=str(s)
    btxt+=txt
if eval(atxt)-eval(btxt)!=0:
    print("Списки не равны")
else:
    print("Списки равны")