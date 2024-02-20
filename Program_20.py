#Remove all occurances of a given element

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

def remove_all_occurances(list1):
    item = input("Enter the item to remove from the list : ")
    list2 = [i for i in list1 if i != int(item)]
    return list2

print("Enter a List : ")
list1=list_input()
converted_list = remove_all_occurances(list1)
print("List after removing all occurances : ",converted_list)