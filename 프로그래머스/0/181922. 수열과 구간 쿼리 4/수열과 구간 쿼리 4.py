def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        quli = []
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
    return arr