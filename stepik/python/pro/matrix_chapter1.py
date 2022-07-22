#4.4-1
"""
a, b = int(input()), int(input())

ResultMatrix = [[""] * b for _ in range(a)]

for i in range(a):
    for j in range(b):
        ResultMatrix[i][j] = input()
    print(*ResultMatrix[i])
"""

#4.4-2
a, b = int(input()), int(input())

ResultMatrix = [[""] * b for _ in range(a)]

for i in range(a):
    for j in range(b):
        ResultMatrix[i][j] = input()
    print(*ResultMatrix[i])

for i in range(b):
    for j in range(a):
        print(*ResultMatrix[j][i])