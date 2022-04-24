"""
Примеры рещения задач с условным оператором if-else
"""

#4.1-1
"""
password1, password2 = input(), input()

if password1 == password2:
    print("Пароль принят")
else:
    print("Пароль не принят")
"""

#4.1-2
"""
if int(input()) % 2 > 0:
    print("Нечетное")
else:
    print("Четное")
"""

#4.1-3
"""
number = int(input())

if (number % 10) + (number % 10 ** 4 // 10 ** 3) == (number % 10 ** 3 // 10 ** 2) - (number % 10 ** 2 // 10 ** 1):
    print("ДА")
else:
    print("НЕТ")

    интересное решение:

a,b,c,d = input()
print('ДА' if int(a) + int(d) == int(b) - int(c) else 'НЕТ')
"""

s = 'ghfdk'
print(dir(s))