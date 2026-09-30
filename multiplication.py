m=int(input("enter the Numbers:"));
n=12345

while n>0:
    m *= n%10
    n//10

    print("multiplication of numbers=",m);
