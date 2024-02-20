def list_input():
    list1=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        item=input("Enter the item : ")
        while(not item.isdigit()):
            item=input("Invalid Item!\nEnter the item : ")
        list1.append(int(item))
        ch=input("Add another item?(y/n) : ")
    return list1

def check_occurence(list):
    item = input("Enter the element to count the occurence : ")
    
    if item.isdigit():
        item=int(item)
    
    counter=0
    for i in list:
        if i==item:
            counter+=1
    return counter

list1=list_input()
count = check_occurence(list1)
print("No of Occurence : ",count)
