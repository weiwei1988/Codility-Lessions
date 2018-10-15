def solution(A):
    sp = 0
    candidate = 0

    for i in range(len(A)):
        if sp == 0:
            sp += 1
            candidate = A[i]
            continue
        
        if candidate == A[i]:
            sp += 1
        else:
            sp -= 1
    
    if sp == 0:
        return 0
    
    cnt = 0
    for i in range(len(A)):
        if A
    
    leader = candidate

    lcnt = 0
    ans = 0

    for i in range(len(A)):
        if A[i] == leader:
            lcnt += 1
        
        lelems = i + 1
        if (lcnt > lelems /2) && ((cnt))


if __name__ == '__main__':
    S = [2, 2, 2, 2, 1, 1]
    print(set(S))
    print(leader(S))