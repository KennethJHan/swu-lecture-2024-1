N = int(input())

for i in range(N):
    score_result = 0
    part_score = 0
    string = input()
    for char in string:
        if char == "O":
            part_score += 1
            score_result += part_score
        else:
            part_score = 0

    print(score_result)
