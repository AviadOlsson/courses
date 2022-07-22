#4.4-1
a, b = int(input()), int(input())

ResultMatrix = [[]]

for i in range(a - 1):
    for j in range(b - 1):
        ResultMatrix[i][j].append(input())

print(ResultMatrix)