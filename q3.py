def sum(n):
    if n <=1:
        return n
    else:
        return n + sum(n-1)
n = int(input("Please enter the number till you want to find sum:"))
print(sum(n))