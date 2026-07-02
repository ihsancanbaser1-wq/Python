num1 = 1.3
num2 = 2.7
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)
num1 = 5
num2 = 10
num3 = 15
## Uncomment to get input from user
## num1 = float(input("Enter the first number: "))
## num2 = float(input("Enter the second number: "))
## num3 = float(input("Enter the third number: "))

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3  
    print("The largest number is:", largest)    
print("Hello, Kubernetes!")
