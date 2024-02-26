num1 = int(input("Enter a number: "))
sign = input("Enter a sign: ")
num2 = int(input("Enter another number: "))

if sign == '+':
   print("summation result: ", num1 + num2)
elif sign == '-':  
     print("subtraction result: ", num1 - num2) 
elif sign == '*':   
    print("Multiplication result: ", num1 * num2) 
elif sign == '/':
    print("division result: ", num1 / num2)
elif sign == '%':
    print("modules result: ", num1 % num2)
else:
    print("invalid Sign:")


                    

