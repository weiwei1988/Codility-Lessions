def solution(S, P, Q):
    counter_a, counter_c, counter_g, counter_t = scanDNA(S)
    IF_list = [0 for i in range(len(P))]

    for i in range(len(P)):
        start = P[i]
        end = Q[i]

        if start == 0:
            if counter_t[end] != 0:
                IF = 4
            if counter_g[end] != 0:
                IF = 3
            if counter_c[end] != 0:
                IF = 2
            if counter_a[end] != 0:
                IF = 1
        else:
            if counter_t[end] - counter_t[start-1] != 0:
                IF = 4
            if counter_g[end] - counter_g[start-1] != 0:
                IF = 3
            if counter_c[end] - counter_c[start-1] != 0:
                IF = 2
            if counter_a[end] - counter_a[start-1] != 0:
                IF = 1

        IF_list[i] = IF
    
    return IF_list
        
def scanDNA(S):
    counter_a = [0 for i in range(len(S))]
    counter_c = [0 for i in range(len(S))]
    counter_g = [0 for i in range(len(S))]
    counter_t = [0 for i in range(len(S))]

    if S[0] == 'A':
        counter_a[0] = 1
    elif S[0] == 'C':
        counter_c[0] = 1
    elif S[0] == 'G':
        counter_g[0] = 1
    elif S[0] == 'T':
        counter_t[0] = 1

    for p in range(1, len(S)):
        if S[p] == 'A':
            counter_a[p] = counter_a[p-1] + 1
            update(p, counter_c, counter_g, counter_t)
        elif S[p] == 'C':
            counter_c[p] = counter_c[p-1] + 1
            update(p, counter_a, counter_g, counter_t)
        elif S[p] == 'G':
            counter_g[p] = counter_g[p-1] + 1
            update(p, counter_a, counter_c, counter_t)
        elif S[p] == 'T':
            counter_t[p] = counter_t[p-1] + 1
            update(p, counter_a, counter_c, counter_g)
    
    return counter_a, counter_c, counter_g, counter_t

def update(p, counter_1, counter_2, counter_3):
    counter_1[p] = counter_1[p-1]
    counter_2[p] = counter_2[p-1]
    counter_3[p] = counter_3[p-1]

if __name__ == '__main__':
    S = 'CAGCCTA'
    P = [2, 5, 0]
    Q = [4, 5, 6]

    print(solution(S, P, Q))

#    print(counter_a)
#    print(counter_c)
#    print(counter_g)
#    print(counter_t)