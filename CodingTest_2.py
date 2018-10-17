def solution(A):
    A_1 = [True for i in A[0] for j in A]
    counter = 0

    for i in range(len(A)):
        for j in range(len(A[i])):
            if not A_1[i][j]:
                continue
            counter += 1
            define_color(A[i][j], A_1, A, i, j)
    return counter

def define_color(v, A_1, A, i, j):
    if i < 0 or j >= len(A):
        return
    if i < 0 or j >= len(A[0]):
        return
    if not A_1[i][j]:
        return
    if A[i][j] != v:
        return
    A_1[i][j] = False

    define_color(v, A_1, A, i+1, j)
    define_color(v, A_1, A, i-1, j)
    define_color(v, A_1, A, i, j+1)
    define_color(v, A_1, A, i, j-1)
