def solution(num_list):
    answer = 0
    pp = 0
    gg = 1
    for i in num_list:
        pp += i
        gg *= i
    pp1 = pp**2
    if gg > pp1:
        return 0
    elif pp1 > gg:
        return 1