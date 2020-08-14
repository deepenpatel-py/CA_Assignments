# TASK SIX: FILE HANDLING AND EXCEPTION HANDLING 

# 1. Write a program in Python to allow the error of syntax to go in exception. HINT: use SyntaxError 

# try:
#     while True
#     print('improper syntax')
# except SyntaxError:
#     print('insert proper sytax')


# 2. Write a program in Python to allow user to open a file by using argv module. If the entered name is incorrect throw an exception and ask them to enter the name again. Make sure to use read only mode.  

import sys

# print('program running')
# filename=sys.argv[1]
# while True:
#     try:
#         fhand=open(filename,'r')
#         print(fhand.read())
#         print('you are in try block')
#         break
#     except:
#         filename=input('Enter the file name again :')
#         print('entered the wrong file name')
#         continue
        
# 3. Write a program to handle an error if the user entered the number more than four digits it should return “Please length is too short/long !!! Please provide only four digits”
# number=input('Enter your number')
# while True:
# 	if len(number)!=4:
# 		raise ValueError('Please length is too short/long !!! Please provide only four digits')
# 	else:
# 		print('Proper Entry')
# 		break

# 4. Create a login page backend to ask user to enter the UserEmail and password. Make sure to ask Re-Type Password and if the password is incorrect give chance to enter it again but it should not be more than 3 times. 

# stored_username = 'deepen'
# stored_password='123456'

# username = input('Enter your user name')
# password = input('Enter your password')


# for i in range(3):
# 	if username == stored_username and password == stored_password:
# 		print('You are logged in')
# 		break
# 	else:
# 		password = input('Enter your password')


# 5. https://www.programiz.com/python-programming/exception-handling Go through this link to understand Finally and Raise concept. 

# 6. Read any file using Python File handling concept and return only the even length string from the doc.txt file. 
# Consider the content as:  

# Hello I am a file  

# Where you need to return the data string  

# Which is of even length  

# Make sure you return the content in  

# The same link as it is present. 

file = 'doc.txt'
fhand=open(file,'r')
for line in fhand:
	if len(line) %2==0 and len(line)!=0:
		print(len(line),line)

fhand.close()
