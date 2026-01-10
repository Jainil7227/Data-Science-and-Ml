def fact(n):
    result=1
    for i in range(1,n+1):
        result=result*i
    return result
n=int(input("Enter a number : "))
print("The factorial of ",n," is ",fact(n))