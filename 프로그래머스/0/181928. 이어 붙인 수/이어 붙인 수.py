def solution(num_list):
    answer = ''
    h = ''
    g = ''
    for i in num_list:
        if i % 2 == 1:
            h += str(i)
        else:
            g += str(i)
    answer = int(h) + int(g)
    return answer