import re
dic={'username':'Amalj$ith','password':'Samaljith@95', 'email':"amaljith21@gmail.com"}
user=[value for value in dic.values()][0]
pswd=[value for value in dic.values()][1]
mail=[value for value in dic.values()][2] 
match=re.search(r'. ^ @ $ * + ? { [ ] \ | ( )',user)
match2=re.search(r'[A-Z]\w+',user)
match3=re.search(r'.+',pswd)
match4=re.search(r'[a-z0-9]@.',mail)
if not match and match2:
    if match3 and len(pswd)>=8:
        if match4:
            print("The User Id is",user[0]+pswd[0]+mail[0])
        else:
            print("Invalid email address")    
    else:
        print("Invalid password syntax")

else:
    print("Invalid user name")   
