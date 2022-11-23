#1.1
"""
print('Я\n\nбудущий\n\nбекенд-разработчик!')
"""

#1.2
"""
print("Привет;мне;нравится;программирование\n\nно писать код что-то не очень.Может поможешь?")
"""

#1.3
"""
inpNumber, inpText = int(input()), input()
print(f"Это число: {inpNumber}\nЭто строка: {inpText}")
"""

#2.1
"""
a, b, c = int(input()), int(input()), int(input())
print((a ** 3 + b ** 0.5) / c)
"""

"""Шпаргалка по переводу в разные системы счисления:
a = 10  # десятичная
# перевод из разных систем счисления в десятичную
b = int('10', 2) # двоичная
c = int('17', 8) # восьмеричная
d = int('1a', 16) # шестнадцатеричная
print(a,b,c,d, end="\n")  # 10 2 15 26

# перевод из десятичной в разные
num = 37
print(bin(num))  # 0b100101
print(oct(num))  # 0o45
print(hex(num))  # 0x25
"""

#2.2
"""
a = int(input())

def aOctInt(num):
    aInt = num // 8
    aRem = num % 8
    return print(aInt, aRem, sep='')

aOctInt(a)
"""

#2.3
"""
time_in_minutes = int(input())

def time_in_hour(time):
    return print(time // 60, time % 60)

time_in_hour(time_in_minutes)
"""

#2.4
"""
time_mins, start_hours, start_mins = int(input()), int(input()), int(input())

def time_out(time_on_mins, start_in_hours, start_in_mins):
    
    hours = 0
    minutes = 0

    if start_in_hours + time_on_mins // 60 > 24:
        hours = (start_in_hours + time_on_mins // 60) - 24
    else:
        hours = start_in_hours + time_on_mins // 60
    
    if start_in_mins + time_on_mins % 60 > 60:
        minutes = (start_in_mins + time_on_mins % 60) - 60
        hours += 1
    else:
        minutes = start_in_mins + time_on_mins % 60

    return print(hours, minutes)

time_out(time_mins, start_hours, start_mins)
"""

#2.5
"""
number = int(input())

def third_number(input_n):
    return print(str(input_n)[1])

third_number(number)
"""

#2.6
"""
float_number = input()

def second_number_after_dot(input_n):
    return print(str(float(input_n) % 1)[3])

second_number_after_dot(float_number)
"""

#2.7
"""
a, b, n = int(input()), int(input()), int(input())

def avarage_time_on_site(minutes, seconds, days):
    all_times_on_site = days * ((minutes * 60) + seconds)
    return print((all_times_on_site // 60) // 60, (all_times_on_site // 60) % 60 ,all_times_on_site % 60)

avarage_time_on_site(a, b, n)
"""

#2.8
"""
import math

a, b, c = float(input()), float(input()), float(input())

def sum_all_float(y, x, z):
    return print(math.fsum((y, x, z)))

sum_all_float(a, b, c)
"""

#2.9
"""
import math

a, b = int(input()), int(input())

def search_gcd(y, x):
    return print(math.gcd(y, x))

search_gcd(a, b)
"""
"""
print(13 << 2 >> 1)
Приколюха с шифрованием

Шифрование:

число ^ ключ = шифрованное число

Дешифрование:

шифрованное число ^ ключ = число
"""

#2.10
"""
encrypted_value = int(input())

def decoder(x):
    return print(x ^ 47)

decoder(encrypted_value)
"""

#2.11
"""
number = int(input())

def chek_condition(number_for_chek):
    f1, f2, f3, f4, f5 = True, True, False, False, False
    
    if number_for_chek % 2 != 0:
        f1 = False
    
    if number_for_chek < 0:
        f2 = False

    if -5 <= number_for_chek <= 5:
        f3 = True
    
    if number_for_chek % 3 == 0 and number_for_chek % 4 == 0 and number_for_chek % 7 != 0:
        f4 = True

    if number_for_chek < 0:
        if len(str(number_for_chek * -1)) == 3:
            f5 = True
    elif len(str(number_for_chek)) == 3:
        f5 = True

    return print(f1, f2, f3, f4, f5, sep="\n")

chek_condition(number)
"""

#2.12
"""
ip_adress = input()

def check_status_ip(input_ip):

    ip_list_string = input_ip.split('.')
    status = True

    for i in range(len(ip_list_string)):
        if 0 <= int(ip_list_string[i]) <= 255:
            status = True
        else:
            status = False
            break

    if ip_list_string[0] == ip_list_string[1] == ip_list_string[2] == ip_list_string[3] == "0" or ip_list_string[0] == ip_list_string[1] == ip_list_string[2] == ip_list_string[3] == "255":
        status = False

    return print(status)

check_status_ip(ip_adress)
"""
#######################################################
#      Шпора по тернарному и маржовому оператору      #
#######################################################
"""
x = int(input())
y = x // 2 if x % 2 == 0 else x * 2


if (x := int(input())) % 2 == 0:
    print(x ** 2 + 5)
else:
    print(x ** 3 - 7)
"""

#2.13
"""
days = int(input())

def day_of_week(number):
    
    list_names = "пн/вт/ср/чт/пт/сб/вс".split('/')

    if number < 7:
        return print(list_names[number])
    elif number % 7 > 7:
        return print(list_names[number % 7 - 7])
    else:
        return print(list_names[number % 7])

day_of_week(days)
"""

#2.14
"""
a, b, c = int(input()), int(input()), int(input())

def minimal_value(n1, n2, n3):

    if n1 <= n2 <= n3 or n1 <= n3 <= n2:
        print(n1)
    elif n2 <= n1 <= n3 or n2 <= n3 <= n2:
        print(n2)
    elif n3 <= n1 <= n3 or n3 <= n3 <= n1:
        print(n3)

minimal_value(a, b, c)
"""

#2.15
"""
login, password = input(), input()

def validation_accaunt(log, pas):

    if len(log) > 4 and len(pas) > 8 and log != pas:
        return print(True)
    else:
        return print(False)

validation_accaunt(login, password)
"""

#2.15
"""
user_command = input()

def bot_answer(command):

    match command:
        case "Привет":
            return print("Привет!")
        case "Как дела?":
            return print("Все классно!")
        case "Пока":
            return print("До скорой встречи!")
        case _:
            return print("Прости, я еще не знаю таких фраз :(")

bot_answer(user_command)
"""

#2.16
"""
name_of_framework = input()

def definition_prof(framework):

    match framework:
        case "Flask" | "Django" | "Fast-API":
            return print(f"Python({framework}),Backend-dev")
        case "Angular" | "React" | "Vue":
            return print(f"JavaScript/TypeScript({framework}),Frontend-dev")
        case "Flutter" | "React Native":
            return print(f"JavaScript({framework}),Cross-Mobile-dev")
        case "Pandas" | "skit-learn" | "keras":
            return print(f"Python({framework}),Data-Scientist")
        case _:
            return print("модель еще не обучена")

definition_prof(name_of_framework)
"""

#############################
#       Раздел "Циклы"      #
#############################

#2.17
"""
a = [print(int(i)) for i in input().split()]
"""

#2.18
"""
value_factorial = int(input())

def factorial_calculation(desired_value):

    factorial = 1

    for i in range(1, desired_value + 1):
        factorial *= i

    return print(factorial)

factorial_calculation(value_factorial)
"""

#2.19

for i in range(1, 3):
    for j in range(2, 2):
        for k in range(3, 5):
            print(k)
    for b in range(3,4):
        for z in range(5,3):
            print(z)
    print(i)