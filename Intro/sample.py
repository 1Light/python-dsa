###################################################################################################
# Create the first 20 first Fibonacci numbers using a loop
###################################################################################################

## using a loop

num1 = 0
num2 = 1

print(num1)
print(num2)

for num in range(18):
    num3 = num1 + num2
    print(num3)

    num1 = num2
    num2 = num3

## using recursion

num1 = 0
num2 = 1

count = 2

print(num1)
print(num2)

def fibonacci(num1, num2):

    global count
    if count <= 19:
        num3 = num1 + num2
        print(num3)

        num1 = num2
        num2 = num3

        count += 1

        fibonacci(num1, num2)
    
    else:
        return

fibonacci(num1, num2)

###################################################################################################
# Find the 20th fibonacci number
###################################################################################################

def fibonacci(num):

    if num <= 1:
        return num
    
    else:
        return fibonacci(num - 1) + fibonacci (num - 2)

print(fibonacci(19))