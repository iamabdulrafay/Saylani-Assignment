# Assignment 5 Question No. 1
for i in range(1, 11):
    print(i)


# Assignment 5 Question No. 2    
for i in range(-1, -21, -1):
    print(i)



# Assignment 5 Question No. 3
for i in range(1, 21):
    if i % 2 == 0:
        print(i)    

# Assignment 5 Question No. 4

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    print(i)        


# Assignment 5 Question No. 5    
num = int(input("Enter a number: "))

for i in range(1, num + 1):
    if i % 2 != 0:
        print(i)

# Assignment 5 Question No. 6
for i in range(5):
    print("Happy Birthday!")

# Assignment 5 Question No. 7
num = int(input("Enter a number: "))

for i in range(1, num+1):
    print(i ** 2)


# Assignment 5 Question No. 8
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num * i}")
   

# Assignment 5 Question No. 9 
start = 3
for _ in range(7):
    print(start)
    start += 4
   

# Assignment 5 Question No. 10   
start = 2
for _ in range(5):
    print(start)
    start *= 3

# Assignment 5 Question No. 11
num = int(input("Enter a number: "))
total = sum(range(1, num + 1))
print(total)


# Assignment 5 Question No. 12
num = int(input("Enter a number: "))
reciprocal = 0
for i in range(1, num+1):
    reciprocal += 1/i
print(reciprocal)



# Assignment 5 Question No. 13
numbers = []
for _ in range(5):
    num = float(input("Enter a number: "))
    numbers.append(num)

print(f"The final running total is: {sum(numbers)}")

# Assignment 5 Question No. 14
def find_factorial():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Factorial does not exist for negative numbers.")
        return
    elif num == 0:
        print("0! is: 1")
        return
    
    total = 1
    for i in range(1, num + 1):
        total *= i
    
    print(f"{num}! is: {total}")


# Assignment 5 Question No. 15
base = int(input("Enter a base number: "))
exponent = int(input("Enter an exponent: "))

result = 1
for _ in range(exponent):
    result *= base

print(result)
