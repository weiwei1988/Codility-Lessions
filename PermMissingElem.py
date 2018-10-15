def solution(A):
    A = sorted(A)
    ans = -1
    c = 0
    if len(A) is 0:
        ans = 1
    
    for i in range(len(A)):
        c += 1

        if A[i] != i + 1:
            ans = i + 1
            break
    
        if c == len(A):
            ans = c + 1

    return ans

if __name__ == '__main__':
    A = []
    print(solution(A))