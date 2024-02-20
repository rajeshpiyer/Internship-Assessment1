#Print Patterns

def input_limit():
    limit=input("Enter the limit : ")
    while(not limit.isdigit()):
        limit=input("Invalid Limit !\nEnter the limit : ")
    return int(limit)

def pattern_1(limit):
    for i in range(1,limit+1):
        for j in range(1,i+1):
            print(" 0 ",end="")
        print()

def pattern_2(limit):
    for i in range(1, limit + 1):
        print(" " * (limit - i), end="")
        print("* " * i)

def pattern_3(limit):
    for i in range(1,limit+1):
        for j in range(1,i+1):
            print(" "+str(i)+" ",end="")
        print()

def pattern_4(limit):
    for i in range(1,limit+1):
        for j in range(1,i+1):
            print(" "+str(j)+" ",end="")
        print()

def pattern_5(limit):
    while(limit>0):
        i=limit
        while(i>0):
            print(" * ",end="")
            i-=1
        limit-=1
        print()

def pattern_6(limit):
    for i in range(1,limit+1):
        for j in range(1,limit+1):
            print(" @ ",end="")
        print()


print("-- PATTERN PRINTING --\n")
limit=input_limit()

print("\nPattern - 1\n")
pattern_1(limit)

print("\nPattern - 2\n")
pattern_2(limit)

print("\nPattern - 3\n")
pattern_3(limit)

print("\nPattern - 4\n")
pattern_4(limit)

print("\nPattern - 5\n")
pattern_5(limit)

print("\nPattern - 6\n")
pattern_6(limit)