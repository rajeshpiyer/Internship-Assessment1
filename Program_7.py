def list_input():
    list1=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        item=input("Enter the item : ")
        list1.append(int(item))
        ch=input("Add another item?(y/n) : ")
    return list1

def binary_search(list,item):
    start,end=0,len(list)-1
    if list[start]==item:
        print("The searched item is found as item no : "+str(start+1)+" in the list.")
    elif list[end]==item:
        print("The searched item is found as item no : "+str(end+1)+" in the list.")
    else:
        mid=end//2
        while(start<end):
            if list[mid]>item:
                end=mid
                mid=(start+end)//2
            elif list[mid]<item:
                start=mid
                mid=(start+end)//2
        if list[mid]==item:
            print("The searched item is found as item no : "+str(mid+1)+" in the list.")
        else:
            print("Item Not Found!")

list1=list_input()
ch='y'
while(ch=='y' or ch=='Y'):
    item=int(input("Enter the item to search : "))
    binary_search(list1,item)
    ch=input("Do you want to search for another item?(y/n) : ")


