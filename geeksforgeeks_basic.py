#sum of two input

num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

sum = num1 + num2

print ("sum:",sum)

#Maximum of two numbers

n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

if n1>n2:
    print (n1)
else:
    print(n2)

#factorial

n = int(input("Enter a number: "))

factorial = 1

if n < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif n == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,n + 1):
       factorial = factorial*i
   print("The factorial of",n,"is",factorial)

#-------------------------------------------------------
#return 1 if (n==1 or n==0) else n * factorial(n - 1) 
   
   def factorial(n):
     
    # single line to find factorial
    return 1 if (n==1 or n==0) else n * factorial(n - 1) 
 
# Driver Code
num = 5
print("Factorial of",num,"is",factorial(num))