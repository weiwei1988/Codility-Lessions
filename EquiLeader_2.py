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
    
    return leader, count

def solution(A):
    leader, N_leader = getleader(A)
    count = 0
    EquiLeader = 0


    for i in range(len(A)):
        if A[i] == leader:
            count += 1
        else:
            pass

        if count > (i+1) // 2 and (N_leader - count) > (len(A) - i - 1) // 2:
            EquiLeader += 1

    return EquiLeader

A = [4, 3, 4, 4, 4, 2]
print(solution(A))
        