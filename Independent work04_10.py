# Напишите программу, в которой на основе двух словарей создается новый словарь. В этот новый словарь включаются те
# элементы, которые представлены в каждом из исходных словарей (имеются ввиду ключи элементов). Значениями элементов
# в создаваемом словаре являются  множества из значений соответствующих элементов в исходных словарях.
A={1:1, 2:2, 3:3, 5:5, 11:11, 25:25}
B={3:'три', 5:'пять', 7:'семь',8:'восемь', 25:'двадцать пять'}
C={n: {v,B[n]} for n,v in A.items() if n in B}
print(C)