def reverse(str):
    str=str.upper()
    if len(str)==0:
        return str
    else:
        return reverse(str[1:])+str[0]
print(reverse('Satyam'))