#Greatest common Divisor

def gcd(a,b):
    for i in range(1,(a//2)+1):
        if a%i==0 and b%i==0:
            gcd=i
    return gcd

print("Greatest Common Divisor\n\n")
a = int(input("Enter First Number : "))
b = int(input("Enter Second number : "))
print("The GCD of "+str(a)+" and "+str(b)+" is "+str(gcd(a,b)))