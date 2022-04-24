#2.1-8
"""
def iosif_flav(num_a, num_b):
    count = 0
    for i in range(1, num_a + 1):
        count = (count + num_b) % i
    return count + 1

print(iosif_flav(int(input()), int(input())))
"""

#2.2-1
"""
def quarters_of_dots(quantity):

    quarter_i, quarter_ii, quarter_iii, quarter_iv = 0, 0, 0, 0

    for i in range(quantity):
        coords = input().split(" ")
        if int(coords[0]) < 0 and int(coords[1]) > 0:
            quarter_ii += 1
        elif int(coords[0]) > 0 and int(coords[1]) > 0:
            quarter_i += 1
        elif int(coords[0]) < 0 and int(coords[1]) < 0:
            quarter_iii += 1
        elif int(coords[0]) > 0 and int(coords[1]) < 0:
            quarter_iv += 1

    return print(f'Первая четверть: {quarter_i}\nВторая четверть: {quarter_ii}\nТретья четверть: {quarter_iii}\nЧетвертая четверть: {quarter_iv}\n')

quarters_of_dots(int(input()))
"""

#2.2-2
"""
list_of_numbers = input().split(" ")

counter = 0
for i in range(len(list_of_numbers)):
    if i + 1 >= len(list_of_numbers):
        break
    else:
        if int(list_of_numbers[i + 1]) > int(list_of_numbers[i]):
            counter += 1
    
print(counter)
"""

#2.2-2
"""
in_list = input().split(" ")
out_list = []
last_elem = []

if len(in_list) % 2 != 0:
    last_elem.append(in_list[-1])
    del in_list[-1]

for i in range(0, len(in_list), 2):
    out_list.append(in_list[i + 1])
    out_list.append(in_list[i])

if len(last_elem) == 1:
    out_list.append(last_elem[0])
    print(" ".join(out_list))
else:
    print(" ".join(out_list))

#Решение с помощью срезов

in_list = input().split()
for i in range(1, len(in_list), 2):
    in_list[i], in_list[i - 1] = in_list[i - 1], in_list[i]
print(*in_list)
"""