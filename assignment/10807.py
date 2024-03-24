N = int(input())
A = input().split()
v = input()
cnt = 0
for elem in A:
    if elem == v:
        cnt += 1

print(cnt)
