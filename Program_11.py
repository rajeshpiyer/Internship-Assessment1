#Intersection
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

print("Enter List 1")
list1=list_input()
print("Enter List 2")
list2=list_input()
print("\n\nIntersection : ",list(set(list1).intersection(set(list2))))
