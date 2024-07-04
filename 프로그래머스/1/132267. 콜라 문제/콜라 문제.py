def solution(a, b, n):
    answer = 0
    while(n >= a):
        real_end = n % a
        n = (n//a) * b
        answer += n
        n += real_end
    return answer