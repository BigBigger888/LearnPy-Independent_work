# Напишите программу, создающую список чисел, которые при делении на 5 дают в остатке 3
#(такие числа вычисляются по формуле 5k + 3, где k = 0,1,2,3...). Отобразить этот список в прямом и обратном порядке.
n=3
nums=[5*k+3 for k in range(n+1)]
print("Список в прямом порядке:", nums)
print("Список в обратном порядке:", list(reversed(nums)))

