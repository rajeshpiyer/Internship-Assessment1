#Anagram or Not

def str_input():
    str=input("Enter a String : ")
    return str

def check_anagram(str1,str2):
    if sorted(str1.lower())==sorted(str2.lower()):
        return True
    else:
        return False

str1=str_input()
str2=str_input()
if check_anagram(str1,str2):
    print("Yes! "+str1+" is the Anagram of "+str2)
else:
    print("No! "+str1+" is not Anagram of "+str2)
