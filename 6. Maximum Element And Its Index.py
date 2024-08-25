def MaxInArray(arr, length):
    max_value = max(arr)
    print(max_value)
    print(arr.index(max_value))

if __name__ == "__main__":
    arr = [1, 3, 7, 2, 5]
    length = len(arr)
    MaxInArray(arr, length)
