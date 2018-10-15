def solution(A, K):
    if A == []:
        return A

    for j in range(K):
        A = one_roate(A)
    
    return A

def one_roate(A):
    A_new = [0 for i in range(len(A))]
    for i in range(1, len(A)):
        A_new[i] = A[i-1]

    A_new[0] = A[len(A) - 1]

    return A_new

if __name__ == '__main__':
    A = []
    print(solution(A, 4))