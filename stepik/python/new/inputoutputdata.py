# Строковый формат данных переменной обозначается кавычками (' или ")
# Целочисленный формат данных - число (1 или 2)
# Для преобразования переменной из строкового формата содержащего цифры в целочисленный формат используется команда int()
# Для преобразования переменной в строковый формат, используется команда str()
# Для переноса строки используется синтаксис '\n'

#2.4-1
#number = int(input())
#print(number, number + 1, number + 2, sep='\n')

#2.4-2
#print(int(input()) + int(input()) + int(input()))

#2.4-3
#edge_length = int(input())
#print('Объем = ' + str(edge_length ** 3), 'Площадь полной поверхности = ' + str(6 * edge_length ** 2), sep='\n')

#2.4-4
#variable_a, variable_b = int(input()), int(input())
#print(3 * (variable_a + variable_b) ** 3 + 275 * variable_b ** 2 - 127 * variable_a - 41)

#2.4-5
#number = int(input())
#print('Следующее за числом ' + str(number) + ' число: ' + str(number + 1), 'Для числа ' + str(number) + ' предыдущее число: ' + str(number - 1), sep='\n')

#2.4-6
#print(3 * (int(input()) + int(input()) + int(input()) + int(input())))

#2.4-7 варик 1
#number_a, number_b = int(input()), int(input())
#print(str(number_a) + ' + ' + str(number_b) + ' = ' + str(number_a + number_b), str(number_a) + ' - ' + str(number_b) + ' = ' + str(number_a - number_b), str(number_a) + ' * ' + str(number_b) + ' = ' + str(number_a * number_b), sep='\n')

#2.4-7 варик 2
#number_a, number_b = int(input()), int(input())
#print(f"{number_a} + {number_b} = {number_a + number_b}\n{number_a} - {number_b} = {number_a - number_b}\n{number_a} * {number_b} = {number_a * number_b}")

#2.4-7 варик 3 - здесь используется свойство .format() которое позвволяет заполнить открытые места ввода переменных в строковый формат для вывода на экран
#a, b = int(input()), int(input())
#print("{} + {} = {}".format(a, b, a + b), "{} - {} = {}".format(a, b, a - b), "{} * {} = {}".format(a, b, a * b), sep='\n')

#2.4-8
#print(int(input()) + int(input()) * (int(input()) - 1))

#2.4-9
#number = int(input())
#print(f'{number}---{number * 2}---{number * 3}---{number * 4}---{number * 5}')

# Опреатор // возвращает целове число от деления
# Оператор % возвращает остаток от деления двух целых чисел

#2.5-1
#print(int(input()) * int(input()) ** (int(input()) - 1))

#2.5-2
#print(int(input()) // 100)

#2.5-3
#quantity_schoolchildren, quantity_tangerine = int(input()), int(input())
#print(quantity_tangerine // quantity_schoolchildren, quantity_tangerine % quantity_schoolchildren, sep='\n')

#2.5-4
#survivors = int(input())
#print(survivors // 2 + survivors % 2)

#2.5-5
#a = int(input())
#print((a + 4 - 1) // 4)

#2.5-6
#minutes = int(input())
#print(f'{minutes} мин - это {minutes // 60} час {minutes % 60} минут.')

# Алгоритм получения цифр n-значного числа
#Последняя цифра: (num % 10 ** 1) // 10 ** 0
#Предпоследняя:(num % 10 ** 2) // 10 ** 1
#Предпредпоследняя:(num % 10 ** 3) // 10 ** 2
#...
#Вторая цифра:(num % 10 ** (n - 1)) // 10 ** (n - 2)
#Первая цифра:(num % 10 ** n) // 10 ** (n - 1)

#2.5-7
#number = int(input())
#print(f'Сумма цифр = {(number % 10) + (number % 100 // 10) + (number // 100)}\nПроизведение цифр = {(number % 10) * (number % 100 // 10) * (number // 100)}')

#2.5-8
#number = int(input())
#print(str(number // 100) + str(number % 100 // 10) + str(number % 10), str(number // 100) + str(number % 10) + str(number % 100 // 10), str(number % 100 // 10) + str(number // 100) + str(number % 10), str(number % 100 // 10) + str(number % 10) + str(number // 100), str(number % 10) + str(number // 100) + str(number % 100 // 10), str(number % 10) + str(number % 100 // 10) + str(number // 100), sep='\n')

#2.5-9
#number = int(input())
#print(f'Цифра в позиции тысяч равна {number % 10 ** 4 // 10 ** 3}\nЦифра в позиции сотен равна {number % 10 ** 3 // 10 ** 2}\nЦифра в позиции десятков равна {number % 10 ** 2 // 10 ** 1}\nЦифра в позиции единиц равна {number % 10 ** 1 // 10 ** 0}')
