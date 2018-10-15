def solution(A):
    B = list(set(A))
    B = sorted(B)

    missing = -1
    count_neg = 0
    count_pos = 0

    for i in range(len(B)):
        if B[i] <= 0:
            count_neg += 1

        elif B[i] > 0:
            if B[i] != count_pos + 1:
                missing = count_pos + 1
                break

            count_pos += 1

    if missing == -1:
        if count_neg == len(B):
            missing = 1
        else:
            missing = B[len(B)-1] + 1
            if missing == 0:
                missing = 1
                
    return missing