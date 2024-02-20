#Sum of elements of a list

def list_input():
    list1 = []
    ch = 'y'
    while ch.lower() == 'y':
        item = input("Enter the item: ")
        while not item.isdigit():
            item = input("Invalid Item!\nEnter the item: ")
        list1.append(int(item))
        ch = input("Add another item? (y/n): ")
    return list1

def sum(list1):
    if list1==[]:
        return 0
    else:
        return list1[0]+sum(list1[1:])

list1=list_input()
sum1=sum(list1)
print("Sum of Elements of the list : ",sum1)




