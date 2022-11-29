#input-->  a4b3c2
#Output--> aaaabbbcc


def convertNumToString(s):
    l=[]
    output=''
    for ch in s:
        if ch.isalpha():
            l.append(ch)
            x=ch
        else:
            d=int(ch)
            output=output+x*d
    return output


s=input("Enter the string:\n")                                       # a4b3c2 
ans=convertNumToString(s)
print(ans)                                                           # aaaabbbcc
