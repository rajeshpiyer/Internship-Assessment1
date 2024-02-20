#Sum of all even numbers in a list
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

def sum_of_even(list1):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    return sum

print("Enter a List : ")
list1=list_input()
sum = sum_of_even(list1)
print("Sum of Even Numbers : ",sum)