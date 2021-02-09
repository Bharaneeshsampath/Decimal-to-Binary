#This code converts Decimal number to a binary number
n=int(input("Enter you Decimal to convert :"))
binary=0
p=1
while n>0:
    lastn=n%2
    binary+=(lastn*p)
    p*=10
    n=n//2
print(binary)
