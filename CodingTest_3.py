def solution(A):
    break_point = 0

    if check_already(A) is True:
        return True

    else:
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                A[i], A[j] = A[j], A[i]
                if check_already(A) is True:
                    break_point = 1
                    break
                else:
                    A[i], A[j] = A[j], A[i]

    if break_point == 1:
        return True
    else:
        return False


def check_already(A):
    break_point = 0
    for i in range(len(A)-1):
        if A[i+1] - A[i] < 0:
            break_point = 1
            break
    
    if break_point == 1:
        return False
    else:
        return True

if __name__ == "__main__":
    A = [1, 3, 5]
    A_1 = [1, 3, 5, 3, 4]
    A_2 = [1, 5, 3, 3, 7]
    A_3 = [1, 2, 1]

    print(solution(A_3))
