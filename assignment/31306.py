vowel = {"a", "e", "i", "o", "u"}
res1 = 0
res2 = 0
s = input()
for c in s:
    if c in vowel:
        res1 += 1
    if c == "y":
        res2 += 1

print(f"{res1} {res1+res2}")
