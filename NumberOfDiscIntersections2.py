import bisect

def solution(A):
    A_1 = [0] * len(A)
    A_2 = [0] * len(A)
    count = 0

    for i in range(len(A)):
        A_1[i] = i + A[i]
        A_2[i] = - (A[i] - i)

    A_1 = sorted(A_1)
    A_2 = sorted(A_2)

    print(A_1)
    print(A_2)

    conbi = int(0.5 * len(A) * (len(A) - 1))

    for i in range(len(A_1)-1):
        a = bisect.bisect_right(A_2, A_1[i])
        count += a
        print(A_1[i], A_2[i+1:], a)

        if count >= 10000000:
            count = -1
            break

    return count - conbi


if __name__ == "__main__":
    A = [1, 5, 2, 1, 4, 0]
    ans = solution(A)
#   ans = bisect.bisect_left([-1, 0, 0, 2, 5], 4)
    print(ans)
    
