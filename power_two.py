def is_power_of_two(n):
    if n == 0:
        return False
    return int(n) == n and (n & (n - 1)) == 0

print(is_power_of_two(31)) 
print(is_power_of_two(64))  