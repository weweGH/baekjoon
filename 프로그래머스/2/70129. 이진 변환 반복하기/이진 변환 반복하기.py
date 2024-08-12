def solution(s):
    num_transformations = 0
    num_zeros_removed = 0

    while s != "1":
        num_zeros_removed += s.count('0')
        s = s.replace("0", "")
        s = bin(len(s))[2:]
        num_transformations += 1

    return [num_transformations, num_zeros_removed]
