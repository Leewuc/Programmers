def solution(a, b):
    answer = str(a) + str(b)
    answer2 = str(b) + str(a)
    if int(answer) > int(answer2):
        return int(answer)
    else:
        return int(answer2)