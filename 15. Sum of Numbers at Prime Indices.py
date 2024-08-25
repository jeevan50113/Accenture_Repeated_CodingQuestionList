def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def SumPrimeIndices(arr):
    if arr is None or len(arr) == 0:
        return -1
    
    return sum(arr[i] for i in range(len(arr)) if is_prime(i))
