data = dict()
alpha_list = list()
for i in range(ord("a"), ord("z") + 1):
    alpha_list.append(chr(i))
    data[chr(i)] = 0

s = input()
for c in s:
    data[c] += 1

for alpha in alpha_list:
    print(data[alpha], end=" ")
