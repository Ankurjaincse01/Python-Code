first=int(input("enter a number"))
operators=input("enter a operators(+,-,*,/,%):")
second=int(input("enter a number "))

if operators == "+":
    print(first+second)

elif operators == "-":
    print(first+-second)

elif operators == "*":
    print(first*second)

elif operators == "/":
    print(first/second)

elif operators == "%":
    print(first%second)

else:
    print(" invalid number ")