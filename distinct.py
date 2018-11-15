def distinct(A):
    stack = {}
    A.sort()
    count = 0

    for i in range(1, len(A)):
        if A[i] != A[i-1]:
            stack[A[i]] = 1
            count += 1

        else:
            stack[A[i]] += 1

    return stack

def solution(A):
    dis = distinct(A)
    result = 0

    for values in dis.values():
        result += values * (values - 1) / 2

    return int(result)

A = [3, 3, 4, 1, 5, 6]
dis = distinct(A)
print(dis)
result = solution(A)
print(result)
            

    