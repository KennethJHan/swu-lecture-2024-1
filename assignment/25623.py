data = list()
for i in range(9):
    data.append(int(input()))

max_val = max(data)
max_idx = data.index(max_val) + 1
print(max_val)
print(max_idx)
