def zone(i, radius):
    return i - radius, i + radius

def count_zone(A):
    for i in range(len(A)):
        count = 0
        x1, x2 = zone(i, A[i])
        for j in range(i+1, len(A)):
            x3, x4 = zone(j, A[j])

            if x2 < x3 or x4 < x1:
                count += 0
            else:
                count += 1
        
        yield count

def solution(A):
    c = count_zone(A)
    count = 0

    for _ in range(len(A)):
        count += c.__next__()

    return count

if __name__ == "__main__":
    A = [1, 5, 2, 1, 4, 0]
    print(solution(A))