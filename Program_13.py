def input_string():
    str = input("Enter a String : ")
    return str

def check_for_integer(str):
    flag=True
    for i in str:
        if not i.isdigit():
            flag=False
    if flag:
        print("Yes!, the String has only numbers.")
    else:
        print("No!, the string has other characters too.")

str = input_string()
check_for_integer(str)