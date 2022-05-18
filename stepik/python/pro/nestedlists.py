#Методы списков
"""
метод append() добавляет новый элемент в конец списка.

метод extend() расширяет один список другим списком.

метод insert() вставляет значение в список в заданной позиции.

метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.

метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.

метод pop() удаляет элемент по указанному индексу и возвращает его.

метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.

метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.

метод copy() создает поверхностную копию списка. 

метод clear() удаляет все элементы из списка.

оператор del позволяет удалять элементы списка по определенному индексу.
"""
#Методы строк работающие со списками
"""
метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов, символ табуляции (\t) или символ новой строки (\n).

метод join() собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.
"""

#4.2-1
"""
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

def appSevenSouthend(anyList):
    return anyList[2][2].append(7000)

appSevenSouthend(list1)

print(list1)
"""

#4.2-2
"""
list1 = ['a', 'b', ['c', ['d', 'e', ['f', 'g'], 'k'], 'l'], 'm', 'n']
sub_list = ['h', 'i', 'j']

def extAnyList(any_list, any_sub_list):
    return any_list[2][1][2].extend(any_sub_list)

extAnyList(list1, sub_list)

print(list1)
"""

#4.2-3
"""
list1 = [[1, 7, 8], [9, 7, 102], [6, 106, 105], [100, 99, 98, 103], [1, 2, 3]]
maximum = -1

def max_elem_list(any_list):
    list_max = []
    for i in range(len(any_list)):
        list_max.append(max(any_list[i]))
    return max(list_max)

maximum = max_elem_list(list1)

print(maximum)
"""

#4.2-4
"""
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

def reverse_elem_list(any_list):
    for i in range(len(any_list)):
        any_list[i].reverse()

reverse_elem_list(list1)

print(list1)
"""

#4.2-5
"""
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

def super_del_list(any_list):
    total = 0
    counter = 0

    for i in range(len(any_list)):
        for j in range(len(any_list[i])):
            total += any_list[i][j]
            counter += 1

    return total / counter

print(super_del_list(list1))
"""
#Решение через сумму элементов вложенных списков
"""
list1 = [[1, 7, 8], [9, 7, 102], [102, 106, 105], [100, 99, 98, 103], [1, 2, 3]]

def super_del_list_sum(any_list):
    total = 0
    counter = 0

    for i in any_list:
        total += sum(i)
        counter += len(i)
        
    return total / counter

print(super_del_list_sum(list1))
"""