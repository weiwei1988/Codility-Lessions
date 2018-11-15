def solution(A):
    max_end = max_slice = 0
    for a in A:
        max_end = max(max_end, max_end + a)
        max_slice = max(max_slice, max_end)
    return max_slice

A = [3, 2, -6, 4, 0]
print(solution(A))