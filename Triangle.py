def solution(A):
    N = len(A)
    A.sort()
    break_point = 0

    for i in range(N-2):

        if A[i] < 0:
            pass
        else:
            if (A[i] + A[i+1] > A[i+2]):
                break_point = 1
                break
    
    if break_point == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    A_1 = [10, 2, 5, 1, 8, 20]
    A_2 = [10, 50, 5, 1]

    print(solution(A_1))
    print(solution(A_2))