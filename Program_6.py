#Queue

def enqueue(list,limit):
    if len(list)>=limit:
        print("Queue is full!")
        return list
    else:
        item=input("Enter the item to add to queue : ")
        list.append(item)
        return list

def dequeue(list):
    if len(list)==0:
        print("Queue is empty")
        return list
    else:
        list.pop(0)
        return list
def display_queue(list):
    if list==[]:
        print("Queue is Empty")
    else:
        print("Queue : ",list)

def queue():
    queue1=[]
    limit=int(input("Enter the limit to create Queue : "))
    ch='y'
    while(ch=='y' or ch=='Y'):
        choice = int(input("\t1.Enqueue\t2.DeQueue\nEnter your choice : "))
        if choice==1:
            queue1=enqueue(queue1,limit)
        elif choice==2:
            queue1=dequeue(queue1)
        display_queue(queue1)
        ch=input("Do you wish to continue?(y/n) : ")

queue()