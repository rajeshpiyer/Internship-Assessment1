#Merge two sorted lists into a single sorted list.
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

def merge_lists(list1, list2):
    list1.sort()
    list2.sort()
    list1.extend(list2)
    list1.sort()
    return list1

print("First List : ")
list1 = list_input()
print("Second List : ")
list2 = list_input()
list3 = merge_lists(list1, list2)
print("Merged & Sorted list:", list3)