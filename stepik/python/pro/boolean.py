#Задачи из темы булево (раздел 3 курса)

#3.1-1
""" решение без шаблона

def func(num1, num2):
    if num1 % num2 == 0:
        return print('делится')
    else:
        return print('не делится')
"""
""" решение с шаблоном stepik

# объявление функции
def func(num1, num2):
    return num1 % num2 == 0

# считываем данные
num1, num2 = int(input()), int(input())

# вызываем функцию
if func(num1, num2):
    print('делится')
else:
    print('не делится')
"""

#