# class Solution:
def countPrimes(n):
    if n <= 2:
        return 0

    numbers = {}
    for p in range(2, int(sqrt(n)) + 1):
        if p not in numbers:
            for multiple in range(p * p, n, p):
                numbers[multiple] = 1

    # Exclude "1" and the number "n" itself.
    return n - len(numbers) - 2

random = countPrimes(75)
print(random)