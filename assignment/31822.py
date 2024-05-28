subject_id = input()
N = int(input())
res = 0
for i in range(N):
    given_id = input()
    if subject_id[:5] == given_id[:5]:
        res += 1

print(res)
