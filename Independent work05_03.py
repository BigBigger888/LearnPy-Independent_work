# Напишите программу, в которой пользователю предлагается ввести текст, а затем в этом тексте, без применения
# специальных методов (а именно, не используюя метод swapcase()), все большие буквы меняются на маленькие,
# а маленькие на большие.
txt=input("Введите текст (на английском языке): ")
new_txt=""
for s in txt:
    if (ord(s)>=ord("A") and ord(s)<=ord("Z")):
        s=chr(ord(s)+32)
    elif (ord(s)>=ord("a") and ord(s)<=ord("z")):
        s=chr(ord(s)-32)
    new_txt+=s
print(new_txt)