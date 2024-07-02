def power(a,b):
    if b ==0:
        return 1
    elif b<0:
        return 1/power(a,-b)
    else:
        return  a*power(a,b-1)
print(power(4,3))