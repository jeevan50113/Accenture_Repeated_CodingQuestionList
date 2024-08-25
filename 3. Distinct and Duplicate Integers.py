def AddDistinctDuplicate(a, b, c, d):
    nums = [a, b, c, d]
    distinct_sum = 0
    duplicate_sum = 0
    for num in nums:
        if nums.count(num) == 1:
            distinct_sum += num
        elif nums.count(num) == 2:
            duplicate_sum = num
    return distinct_sum - duplicate_sum

if __name__ == "__main__":
    a, b, c, d = 1,2,2,4
    print(AddDistinctDuplicate(a, b, c, d))
