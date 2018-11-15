def solution(S):
    left_braket = 0

    for w in S:
        if w == '(':
            left_braket += 1
        elif w == ')':
            if left_braket == 0:
                return 0
            else:
                left_braket -= 1

    if left_braket == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    S_1 = "(()(())())"
    S_2 = "())"

    print(solution(S_1))
    print(solution(S_2))
