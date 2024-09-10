def Weirdo(A: list):
    n = len(A)
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count += 1
            adpt_j = j + 1
            if A[n - adpt_j + 1] != j:
                return count
        count += 1
        adpt_i = i - 1
        if (A[adpt_i] != n - i + 1) or (A[0] + A[1] == 2 * n - 1):
            return count
    return count


test1 = [5, 4, 3, 2, 1]
test2 = [1, 2, 3, 4, 5]

print(Weirdo(test1))
