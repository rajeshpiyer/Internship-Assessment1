#Number of Vowels

def vowel_count(str):
    count=0
    for i in str:
        if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
            count+=1
    return count

str=input("Enter a String : ")
count = vowel_count(str)
print("Count of vowels = ",count)
