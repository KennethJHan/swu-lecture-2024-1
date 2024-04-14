A = int(input())
B = int(input())
C = int(input())

res = str(A * B * C)

data = dict()

for i in res:
    if i not in data:
        data[i] = 0

    data[i] += 1

for i in range(0, 10):
    print(data.get(str(i), 0))
