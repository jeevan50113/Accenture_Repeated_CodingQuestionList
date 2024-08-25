def FineNumber(a, b, n, m):
    max_diff = float('-inf')
    for i in a:
        for j in b:
            max_diff = max(max_diff, abs(i - j))
    return max_diff

if __name__ == "__main__":
    a = [1, 3, 5]
    b = [9, 2, 8]
    n = len(a)
    m = len(b)
    print(FineNumber(a, b, n, m))
