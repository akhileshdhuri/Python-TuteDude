#Task 1: Check if a Number is Even or Odd

num=int(input('Enter a number: '))
if num % 2 == 0:
    print(num,'is an Even number')
else:
    print(num,'is an Odd number')

#Task 2: Sum of Integers from 1 to 50 Using a Loop

x=list(range(1,51))
total = 0
for i in x:
    total += i
print("The sum of numbers from 1 to 50 is:", total)
