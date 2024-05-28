ca, ba, pa = list(map(int, input().split()))
cr, br, pr = list(map(int, input().split()))

res = 0

if ca < cr:
    res += cr - ca
if ba < br:
    res += br - ba
if pa < pr:
    res += pr - pa

print(res)
