def countdown(n,i):
    if i == n+1:
        print ("Boooommmmm")
    else:
        print (i)
        countdown(n,i+1)
i=0
countdown(5,i)