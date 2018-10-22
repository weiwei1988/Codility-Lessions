def solution(A, B, M, X, Y):
    people_weight = 0
    people_N = 0
    go_floor = []
    N_floor = 0
    i = 0

    while True:
        people_N += 1
        people_weight += A[i]
        go_floor.append(B[i])


        if people_N == X or people_weight >= Y:
            if people_N == X or people_weight == Y:
                N_floor += len(set(go_floor)) + 1
                people_N, people_weight, go_floor = reset(people_N, people_weight, go_floor)
            else:
                people_N -= 1
                people_weight -= A[i]
                del go_floor[-1]
                i -= 1

                N_floor += len(set(go_floor)) + 1
                people_N, people_weight, go_floor = reset(people_N, people_weight, go_floor)

        elif i == len(A) - 1:
            N_floor += len(set(go_floor)) + 1
            people_N, people_weight, go_floor = reset(people_N, people_weight, go_floor)
            break
        
        i += 1
            
    return N_floor
            
def reset(people_N, people_weight, go_floor):
    people_N = 0
    people_weight = 0
    go_floor = []

    return people_N, people_weight, go_floor

if __name__ == "__main__":
    """乗る人の体重"""
    A = [100, 100, 50, 50, 40]
    A_2 = [60, 80, 40]
    A_3 = [30]

    """行きたい階"""
    B = [2, 2, 3, 2, 3]
    B_2 = [2, 3, 3]

    """階の数"""
    M = 3
    M_2 = 5

    """人数制限"""
    X = 5
    X_2 = 2

    """体重制限"""
    Y = 200
    Y_2 = 200

    print(solution(A, B, M, X, Y))
    print(solution(A_2, B_2, M_2, X_2, Y_2))