data = dict()
for i in range(5):
    s = input()
    if s not in data:
        data[s] = 0

    data[s] += 1

for key, val in data.items():
    if val != 2:
        print(key)
