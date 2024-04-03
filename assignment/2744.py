data = input()
result = ""

for char in data:
    if char.isupper():
        result += char.lower()
    else:  # char.islower()
        result += char.upper()

print(result)
