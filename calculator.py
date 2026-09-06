a=int(input("Enter the operand1:"))
b=int(input("Enter the operand2:"))
operator=input("Enter the operator:")
if operator=='+':
    c=a+b
    print(c)
elif operator=='-':
    c=a-b
    print(c)
elif operator=='*':
    c=a*b
    print(c)
elif operator=='/':
    c=a/b
    print(c)
elif operator=='%':
    c=a%b
    print(c)
elif operator=='**':
    c=a**b
    print(c)
else:
    print("invalid operator")