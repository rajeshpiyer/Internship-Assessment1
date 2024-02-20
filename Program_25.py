#Number of occurrences of each element in a tuple
def char_count(tuple1):
    occurrences = {}
    for i in tuple1:
        if i in occurrences:
            occurrences[i] += 1
        else:
            occurrences[i] = 1
    return occurrences

def input_tuple():
    tuple1 = input("Enter a tuple (separate elements with commas and enclose within parentheses): ")
    tuple1 = tuple1.strip("()").strip()
    
    items = tuple1.split(",")
    tuple1 = tuple(int(item) for item in items)
    
    return tuple1

tuple1 = input_tuple()
occurrences = char_count(tuple1)
print("Number of occurrences of each element : ")
for element, count in occurrences.items():
    print(element, ":", count)
