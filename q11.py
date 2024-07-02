def numberOfSteps(n, steps=0):
    if n == 0:
        return steps
    elif n % 2 == 0:
        return numberOfSteps(n // 2, steps + 1)
    else:
        return numberOfSteps(n - 1, steps + 1)

print(numberOfSteps(14))  