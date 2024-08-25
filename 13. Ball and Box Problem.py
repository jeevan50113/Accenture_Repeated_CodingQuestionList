def NumberOfBalls(arr, n):
    if not arr:
        return -1
    total = 0
    for i in range(n):
        required = (i + 1) ** 2
        total += max(0, required - arr[i])
    return total

if __name__ == "__main__":
    arr = [1, 4, 9, 16]
    n = len(arr)
    print(NumberOfBalls(arr, n))
