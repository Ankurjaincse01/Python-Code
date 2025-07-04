def factorial(x):
    if x == 1:
        return 1
    else:
        # Calling recursion function
        return(x*factorial(x-1))
num = int(input("Num : "))
print("The factorial of ",num,"is : ",factorial(num))