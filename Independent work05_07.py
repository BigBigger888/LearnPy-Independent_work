# Напишите программу для шифрования и дешифрования текста. Текст шифруется так: каждая буква заменяется на ту, что
# размещена от нее на три позиции влево. Вторая буква в алфавите заменяется на последнюю. Первая буква в алфавите
# заменяется на предпослеюнюю.
txt=input("Введите текст: ")
new_txt=""
n=ord("а")
m=ord("я")
N=ord("А")
M=ord("Я")
for s in txt:
    k=ord(s)
    if (k>(n+1) and k<m) or (k>(N+1) and k<M):
         s=chr(k-2)
    elif k == n:
        s=chr(m-2)
    elif k==N:
        s=chr(M-2)
    elif k==(n+1):
        s = chr(m - 1)
    elif k==(N+1):
        s=chr(M-1)
    new_txt+=s
print("Шифр", new_txt)