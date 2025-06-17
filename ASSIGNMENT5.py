Task 1: Create a Dictionary of Student Marks

student_marks = {'Andy':85,'Jack':75,'Rachel':50}
name = input('Enter your name to get the marks scored: ').title()

if name in student_marks:
    print(f'Hey {name}, you have scored {student_marks[name]}')
else:
    print(f"Sorry, no marks found for {name}.")


Task 2: Demonstrate List Slicing

numbers = [1,2,3,4,5,6,7,8,9,10]
first_five = numbers[:5]

reversed_first_five = first_five[::-1]


print('First five elements:', first_five)
print('Reversed list:', reversed_first_five)
