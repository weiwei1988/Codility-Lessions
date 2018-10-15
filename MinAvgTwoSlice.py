def solution(A):

    if len(A) < 3:
        i_min_d, avg_d = double_check(A)
        return i_min_d
    else:
        i_min_d, avg_d = double_check(A)
        i_min_t, avg_t = triple_check(A)

        if avg_d < avg_t:
            return i_min_d
        else:
            return i_min_t

def double_check(A):

    avg = (A[0] + A[1]) / 2.0
    i_min = 0

    for i in range(len(A)-1):
        avg_new = (A[i] + A[i+1]) / 2.0

        if avg_new < avg:
            i_min = i
            avg = avg_new

    return i_min, avg

def triple_check(A):
    avg = (A[0] + A[1] + A[2]) / 3.0
    i_min = 0

    for i in range(len(A)-2):
        avg_new = (A[i] + A[i+1] + A[i+2]) / 3.0
        if avg_new < avg:
            i_min = i
            avg = avg_new

    return i_min, avg

if __name__ == "__main__":
    A = [-3, -5, -8, -4, -10]
    i_min_1, avg_1 = double_check(A)
    i_min_2, avg_2 = triple_check(A)
    ans = solution(A)

    print(i_min_1, avg_1)
    print(i_min_2, avg_2)
    print(ans)