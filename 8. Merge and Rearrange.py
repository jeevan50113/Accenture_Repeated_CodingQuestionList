def MergeStrings(str1, str2):
    i, j = 0, 0
    n = len(str1) + len(str2)
    result = [''] * n
    for k in range(n):
        if i < len(str1) and (j >= len(str2) or str1[i] < str2[j]):
            result[k] = str1[i]
            i += 1
        else:
            result[n - 1 - k] = str2[j]
            j += 1
    return ''.join(result)

if __name__ == "__main__":
    str1 = "acxz"
    str2 = "bd"
    print(MergeStrings(str1, str2))
