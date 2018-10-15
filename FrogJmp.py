def solution(X, Y, D):
    ans = (Y - X) / D
    mod = (Y - X) % D

    if mod == 0:
        return int(ans)
    else:
        return int(ans) + 1


if __name__ == "__main__":
    print(solution(10, 85, 30))
    print(solution(1, 5, 2))
    print(solution(1, 11, 5))