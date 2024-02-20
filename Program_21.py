#Remove white spaces in a string

def remove_space(str):
    str2=""
    for i in str:
        if i!=" ":
            str2+=i
    return str2

str = input("Enter a String : ")
str2 = remove_space(str)
print("String after removing white space : ",str2)