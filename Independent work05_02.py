# Напишите программу, в которой с использованием операторов цикла и форматированных литералов, символом "звездочка" *
# в области вывода отображается буква "А".
A="{0:{2}{1}s}"
num=7
k=7
#for k in range(1,num+1):
while k>1:
    if k == 4:
        print(A.format("*", k, ">"), end="")
        print(" *  * ", end="")
        print(A.format("*", k, "<"))
        k-=1
    print(A.format("*",k,">"),end="")
    print(" "*(2*(num-k)),end="")
    print(A.format("*",k,"<"))
    k-=1