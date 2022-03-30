# Напишите программу, в которой пользователь вводит две даты, а программа определяет количество полных дней между
# этими датами.
from datetime import date
print("Введите две даты в формате год-месяц-день")
firstDate=input("Введите первую дату: ")
secondDate=input("Введите вторую дату: ")
fD=date.fromisoformat(firstDate)
sD=date.fromisoformat(secondDate)
delta=sD-fD
print("Количество полных дней между датами:", abs(delta))