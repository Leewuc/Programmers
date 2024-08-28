def solution(arr, queries):
    answer = []
    for s,e,k in queries:
        quli = []
        for i in range(s,e+1):
            if arr[i] > k:
                quli.append(arr[i])
        if quli:
            answer.append(min(quli))
        else:
            answer.append(-1)
    return answer