def NextSmallerNumber(a, m):
    result = [-1] * m
    for i in range(m):
        for j in range(i + 1, m):
            if a[j] < a[i]:
                result[i] = a[j]
                break
    return result

if __name__ == "__main__":
    a = [4, 2, 6, 5]
    m = len(a)
    print(NextSmallerNumber(a, m))
