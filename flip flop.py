def palindrome(t):
    e = len(t) -1
    s= 0 
    while (s<e):
        if(t[s]!=t[e]):
            return False 
        s+=1
        e-=1
    return True
t =(1,2,2,3,5,4,3,2,2,1)
if(palindrome(t)):
    print("The tuple is Flip-Flop!")
else:
    print("The tuple is not Flip-Flop!")