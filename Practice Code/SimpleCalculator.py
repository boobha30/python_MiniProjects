num1=input("Enter first number: ")
num2=input("Enter second number: ") 
operator=input("Enter operator: ")
if operator=="+":
    print(num1,"+",num2,"=",float(num1)+float(num2))
elif operator=="-":
    print(num1,"-",num2,"=",float(num1)-float(num2))
elif operator=="*":
    print(num1,"*",num2,"=",float(num1)*float(num2))
elif operator=="/":
    print(num1,"/",num2,"=",round((float(num1)/float(num2)),2))
else:    print("Invalid operator")  
