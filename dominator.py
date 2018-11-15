def solution(A):
    leader = getleader(A)

    if leader == -1:
        return -1
    else:
        for idx in range(len(A)):
            if A[idx] == leader:
                return idx

def getleader(A):
    
    n = len(A)
    size = 0

    for k in range(n):
        if size == 0:
            size += 1
            value = A[k]
        else:
            if value != A[k]:
                size -= 1
            else:
                size += 1

    candidate = -1
    if size > 0:
        candidate = value
    leader = -1
    count = 0

    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    
    return leader

A = [3, 4, 3, 2, 3, -1, 3, 3]
print(solution(A))