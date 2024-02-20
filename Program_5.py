#Stack

def push(list,limit):
    if len(list)>=limit:
        print("Stack Overflow!")
        return list
    else:
        item=input("Enter the item to push to stack : ")
        list.append(item)
        return list

def pop(list,limit):
    if len(list)==0:
        print("Stack Underflow!")
        return list
    else:
        list.pop()
        return list
def display_stack(list):
    if list==[]:
        print("Stack is Empty")
    else:
        print("Stack : ",list)

def stack():
    stack1=[]
    limit=int(input("Enter the limit to create Stack : "))
    ch='y'
    while(ch=='y' or ch=='Y'):
        choice = int(input("\t1.Push\t2.Pop\nEnter your choice : "))
        if choice==1:
            stack1=push(stack1,limit)
        elif choice==2:
            stack1=pop(stack1,limit)
        display_stack(stack1)
        ch=input("Do you wish to continue?(y/n) : ")

stack()
    
