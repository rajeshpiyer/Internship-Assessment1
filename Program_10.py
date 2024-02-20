#Remove Duplicates

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

list1=list_input()
converted_list = list(set(list1))
print("Original List : ",list1)
print("After Conversion : ",converted_list)