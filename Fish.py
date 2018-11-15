def scan(A, B):
    N = len(B)
    loop = 0

    while (loop <= 10):
        i = 1
        update = 0

        while(i<N):
            if B[i-1] == 1 and B[i] == 0:

                if A[i-1] < A[i]:
                    A[i-1] = A[i]
                    A[i] = 0
                    B[i-1] = 0
                    B[i] = -1

                    update += 1
                    i += 1

                elif A[i-1] > A[i]:
                    A[i] = A[i-1]
                    A[i-1] = 0
                    B[i] = 1
                    B[i-1] = -1

                    update += 1
                    i += 2
            else:
                i += 1
        
        loop += 1
        if update == 0:
            break
        print(A)
        print(B)
        print(loop)



A = [4, 3, 2, 1, 5, 1]
B = [0, 1, 0, 0, 1, 0]

scan(A,B)