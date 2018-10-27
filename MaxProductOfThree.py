def solution(A):
    x1 = -1001
    x2 = -1002
    x3 = -1003
    
    y1 = 1001
    y2 = 1002

    if len(A) == 3:
        return A[0] * A[1] * A[2]

    else:
        for i in range(len(A)):
            if A[i] > x1:
                x3 = x2
                x2 = x1
                x1 = A[i]

            elif A[i] > x2 and A[i] < x1:
                x3 = x2
                x2 = A[i]

            elif A[i] > x3 and A[i] < x2:
                x3 = A[i]

            if A[i] < y1:
                y2 = y1
                y1 = A[i]
            elif A[i] < y2:
                y2 = A[i]

        ans_1 = x1 * x2 * x3
        ans_2 = y1 * y2 * x1

        if ans_1 >= ans_2:
            return ans_1
        else:
            return ans_2


if __name__ == '__main__':
    A = [-2, -2, 5, 6]
    print(solution(A))