def solution(A):
    A = A.sort()

    for i in range(len(A)-2):
        if A[i] < 0:
            pass
        else:
            if (A[i] + A[i+1] > A[i+2]):
                return 1
                break
    
    return 0

if __name__ == '__main__':
    A_1 = [10, 2, 5, 1, 8, 20]
    A_2 = [10, 50, 5, 1]

    print(solution(A_1))
    print(solution(A_2))