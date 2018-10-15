def solution(N):
    binary = bin(N)[2:]
    binary_gap = 0
    binary_gap_new = 0

    for i in range(len(binary)):
        if binary[i] == str(1):
            for j in range(i+1, len(binary)):
                if binary[j] == str(1):
                    binary_gap_new = j - i - 1
                    binary_gap = max(binary_gap, binary_gap_new)
                    break
    return binary_gap
                    

if __name__ == "__main__":
    print(bin(9)[2:], solution(9))
    print(bin(90)[2:], solution(90))
    print(bin(900)[2:], solution(900))
    print(bin(912312414)[2:], solution(912312414))