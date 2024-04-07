N = input()
data = list(map(int, input().split()))

min_value = data[0]
max_value = data[0]

for i in data:
    if min_value > i:
        min_value = i
    if max_value < i:
        max_value = i

print(min_value, max_value)
