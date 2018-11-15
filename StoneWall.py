def solution_slow(H):
    N = len(H)
    A = [1 for i in range(N)]


    for i in range(1, N):
        temp = None

        if H[i] == H[i-1]:
            A[i] = A[i-1]

        else:
            for j in range(i-1, -1, -1):
                if H[j] < H[i]:
                    A[i] = A[i-1] + 1
                    temp = 1
                    break
                
                elif H[j] == H[i]:
                    A[i] = A[i-1]
                    temp = 1
                    break
                
            if temp == None:
                A[i] = A[i-1] + 1        
    
    return A[N-1]


def solution(H):
    N = len(H)
    stack = [0 for i in range(N)]
    stones = 0
    stack_num = 0

    for i in range(N):
        while stack_num > 0 and stack[stack_num - 1] > H[i]:
             stack_num -= 1
        if stack_num > 0 and stack[stack_num - 1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
            
    return stones



if __name__ == '__main__':
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    print(H)
    print(solution(H))

