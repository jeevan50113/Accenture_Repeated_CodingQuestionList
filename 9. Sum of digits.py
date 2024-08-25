def DifferenceSumOfDigits(arr, n):
    F1 = sum(sum(int(digit) for digit in str(num)) for num in arr) % 10
    F2 = sum(arr) % 10
    return F1 - F2

if __name__ == "__main__":
    arr = [123, 456, 789]
    n = len(arr)
    print(DifferenceSumOfDigits(arr, n))
