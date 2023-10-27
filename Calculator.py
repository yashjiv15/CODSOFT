# Welcome to the Python based calculator

num1=float(input("Enter any number"))
num2=float(input("Enter another number"))


print("Input 1 for Addition:") 
print("Input 2 for Subtraction:") 
print("Input 3 for Multiplication:") 
print("Input 4 for Division:") 


op=int(input("Enter any operation from 1 to 4:-"))

if op==1:
	print("Addition of two numbers is",num1+num2)
elif op==2:
	print("Substraction of two numbers is",num1-num2)
elif op==3:
	print("Multiplicatoin of two numbers is",num1*num2)
elif op==4:
	print("Division of two numbers is",num1/num2)
else:
	print("Invalid input")



