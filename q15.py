def palindrome(str):
    str = str.lower()
    if len(str)==0:
        return str
    else:
        return palindrome(str[1:])+str[0]
    
str="Madam"
if (palindrome(str)==str.lower()):
    print("String ",str,"is palindrome and it's palindrome is:",palindrome(str))
else:
    print("String {str} is not palindrome:",palindrome(str))