#Perfect number or not
def perfect_number(num):
    if num <= 0:
        print(number, "is not a perfect number.") 
    
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(number, "is a perfect number.")
    else:
        print(number, "is not a perfect number.") 


number = int(input("Enter a number: "))
perfect_number(number)
