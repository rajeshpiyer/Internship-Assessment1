#Reverse a list

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

def reverse(list):
    return sorted(list, reverse=True)

list1=list_input()
print("Before sorting : ",list1)
list1 = reverse(list1)
print("After Sorting : ",list1)