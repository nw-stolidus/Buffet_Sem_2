print("Enter a number: ")
num1 = input()

print("Enter the operation: ")
oper = input()

print("Enter the second number: ")
num2 = input()

mult = "*"
div = "/"
sub = "-"
add = "+"
answer = 0
num1 = int(num1)
num2 = int(num2)

if oper == "*": 
    answer = num1 * num2
    answer = str(answer)
    num1 = str(num1)
    num2 = str(num2)
    print(num1+oper+num2+" = "+ answer)
elif oper == "/":
    answer = num1 / num2
    answer = str(answer)
    num1 = str(num1)
    num2 = str(num2)
    print(num1+oper+num2+" = "+ answer)
elif oper == "-":
    answer = num1 - num2
    answer = str(answer)
    num1 = str(num1)
    num2 = str(num2)
    print(num1+oper+num2+" = "+ answer)
elif oper == "+":
    answer = num1 + num2
    answer = str(answer)
    num1 = str(num1)
    num2 = str(num2)
    print(num1+oper+num2+" = "+ answer)
else:
    print("Incorrect input please try again!")
    
    
    
    