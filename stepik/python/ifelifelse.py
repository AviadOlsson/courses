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


#интересное решение:

a,b,c,d = input()
print('ДА' if int(a) + int(d) == int(b) - int(c) else 'НЕТ')
"""

#4.1-4
"""
age = int(input())

if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#Пример однострокового решения:

print("Доступ разрешен" if int(input()) >= 18 else "Доступ запрещен")
"""

#4.1-5
"""
number_a, number_b, number_c = int(input()), int(input()), int(input())

if number_c - number_b == number_b - number_a:
    print("YES")
else:
    print("NO")
"""

#4.1-6
"""
number_a, number_b = int(input()), int(input())

if number_a > number_b:
    print(number_b)
else:
    print(number_a)
"""

#4.1-7
"""
#Решение без if, с помощью списка

list_numbers = [int(input()), int(input()), int(input()), int(input())]
print(min(list_numbers))

#Решение через if

number_a, number_b, number_c, number_d = int(input()), int(input()), int(input()), int(input())

temporary_ab, temporary_cd = 0, 0

if number_a > number_b:
    temporary_ab = number_b
else:
    temporary_ab = number_a

if number_c > number_d:
    temporary_cd = number_d
else:
    temporary_cd = number_c

if temporary_ab > temporary_cd:
    print(temporary_cd)
else:
    print(temporary_ab)
"""

#4.1-8
"""
age = int(input())

if age <= 13:
    print("детство")
elif 14 <= age < 24:
    print("молодость")
elif 25 <= age < 59:
    print("зрелость")
else:
    print("старость")
"""

#4.1-9
"""
number_a, number_b, number_c = int(input()), int(input()), int(input())

adder = 0

if number_a > 0:
    adder += number_a

if number_b > 0:
    adder += number_b

if number_c > 0:
    adder += number_c

print(adder)
"""