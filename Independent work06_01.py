# Напишите программу, в которой создается функция с двумя аргументами, являющимися числовыми списками.
# Результатом является число, равное сумме попарных произведений элементов списков. Если в одном из списков
# элементов меньше, чем в другом, то недостающие элементы получают путем циклического повторения содержимого списка.
def doubble(a,b):
    c=list()
    if type(a)!=list or type(b)!=list:
        return print("Оба аргумента должны быть списками!")
    else:
        if len(a)>len(b):
            k=len(a)-len(b)
            for i in range(k):
                b.append(b[i])
        else:
            k = len(b) - len(a)
            for i in range(k):
                a.append(a[i])
        for s in range(len(a)):
            c.append(a[s]*b[s])
    return print(c)
doubble([1,2,3,4],[1,2,3,4,5])