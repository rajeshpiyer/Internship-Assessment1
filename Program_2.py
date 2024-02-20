#Password Validation
def pass_input():
    password = input("Enter Password : ")
    return password

def validate():
    password = pass_input()
    counter = 0
    explanation = ""
    
    if len(password)<8:
        counter +=1
        explanation += "\n"+str(counter)+". Password should contain atleast 8 characters."

    char_flag=0
    int_flag=0
    special_flag=0
    for i in password:
        if i.isupper():
            char_flag=1
        elif i.isdigit():
            int_flag=1
        elif i=='@' or i=='$' or i=='_':
            special_flag=1
    if char_flag==0:
        counter+=1
        explanation += "\n"+str(counter)+". Password should contain atleast 1 upper case alphabet."
    if int_flag==0:
        counter+=1
        explanation += "\n"+str(counter)+". Password should contain atleast 1 number."
    if special_flag==0:
        counter+=1
        explanation += "\n"+str(counter)+". Password should contain atleast 1 of '@' or '_' or '$'."

    if counter==0:
        print("!YES! -- The Password is Valid!")
    else:
        print("!!! -- PASSWORD INVALID -- !!!")
        print(explanation+"\n\n")

validate()




