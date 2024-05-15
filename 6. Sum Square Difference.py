def sumSquares(n):
    total = 0
    for i in range(1, n+1):
        total = total + i*i

    # (n)(n+1)(2n+1)/6

    return total

def squareofSum(n):
    total = 0
    for i in range(1, n+1):
        total = total + i

    # n(n+1)/2 * n(n+1)/2

    return total*total

def diff(n):
    print(squareofSum(n) - sumSquares(n))

diff(100)

# can be O(1) time with formulas