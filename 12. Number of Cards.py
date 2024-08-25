def CardsPyramid(n):
    if n == 0:
        return -1
    cards = n * (3 * n + 1) // 2
    return cards % 1000007

if __name__ == "__main__":
    n = 3
    print(CardsPyramid(n))
