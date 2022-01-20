from re import S



s="Dancing"
def verbal(s):
    if len(s)>=3 and s[-3:]!="ing":
        s=s+"ing"
    else:
        s=s+"ly"    
       
        
    return s    
print(verbal(s))            