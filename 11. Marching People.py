def MaximumBarrier(n, barrier):
    blocked = set()
    for b in barrier:
        x, y, d = b
        for i in range(x, x + d + 1):
            blocked.add(i)
    return len(blocked)

if __name__ == "__main__":
    n = 10
    barrier = [(1, 1, 3), (5, 1, 2)]
    print(MaximumBarrier(n, barrier))
