def count_zero(num,count):
    if num==0:
        return count 
    elif num %10 ==0:
        return count_zero( num//10,count +1)
    else:
        return count_zero(num//10,count)
    
print(count_zero(100,0))