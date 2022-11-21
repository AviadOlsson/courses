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

float_number = input()

def two_number_after_dot(input_n):
    return print(int(input_n) % 100)

two_number_after_dot(float_number)