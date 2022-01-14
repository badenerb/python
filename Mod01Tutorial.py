#Baden Erb

#Task 1
print ('\nTask 1')
print ('Hello World')
input()

#Task 2
print ('\nTask 2')
user_guess = input('Please enter an integer: ')
print(user_guess)
input()

#Task 3
print ('\nTask 3')
user_guess = int(user_guess)
converted_user_guess = int(user_guess)
print(user_guess * 3)
print(converted_user_guess * 3)
user_guess = str(user_guess)
print(user_guess * 3)
print('I entered' + user_guess)
#print ('I entered' + converted_user_guess)
#This line throws an error!

#Task 4
print ('\nTask 4')
for i in range (1,21,1):
    if i == 7:
        print ('snowflake')
    elif(0 == i % 2):
        print ('even')
    else:
        print ('odd')
        
#Task 5
print ('\nTask 5')
print('What number would you like to try, that is greater than 13?')
number = input()
con_num = int(number) + 1
for i in range (1,con_num,1):
    if i == 7:
        print ('lucky')
    elif i == 13:
        print ('unlucky')
    elif(0 == i % 2):
        print ('even')
    else:
        print ('odd')

#Task 6
print ('\nTask 6')
while (True):
    last_name = input("What's your last name(Erb)? ")
    if last_name == 'Erb':
        break

#Task 7
print ('\nTask 7')
counter = 0
while(counter < 10):
    print (counter)
    counter += 1

#Task 8
print ('\nTask 8')
import random

for i in range(0,5,1):
    random_int = random.randint(-10,10)
    print (random_int, end = " ")

print()
print()
print('Press Enter to end the script')
input()
