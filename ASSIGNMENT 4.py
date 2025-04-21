#Task 1: Read a File and Handle Errors

file_name = 'sample.txt'
try:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        for index, line in enumerate(lines, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print(f"The file {file_name} was not found.")


#Task 2: Write and Append Data to a File

m=str(input('Enter text to write to the file: '))
file1 = open('output.txt','a')
appending_file = file1.write(m + '\n')
print(appending_file)
file1.close()
file1 = open('output.txt','r')
reading_file = file1.read()
print(reading_file)
file1.close()



