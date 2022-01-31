#Baden Erb
#Mod 02 Tutorial

import random
import sys

counter = 0
user_list = []
int_list = []

while counter< 10:
    list_item = input('Please enter a number or word to use in the list: ')
    user_list.append(list_item)
    counter += 1

def random_insert(name):
    list_pos = random.randint(0,9)
    user_list.insert(list_pos, name)

#Task 1- Check the length of the list
print('Task 1')
print('The list has ten items. ' + str(len(user_list) == 10))

#Task 2- Print the List
print('\nTask 2')
print(user_list)

#Task 3- The Swap
print('\nTask 3')
spot1 = user_list[0]
user_list[0] = user_list[9]
user_list[9] = spot1

print(user_list)

#Task 4- Print the first three items and the last three
print('\nTask 4')
print(user_list[0:3], user_list[-3:])

#Task 5- Loop through and print all the items in the list
print('\nTask 5')
for i in user_list:
    print(i)

#Task 6- Use an IF statement to check to see if the word "cat" is in the list and let the user know.
print('\nTask 6')
if 'cat' in user_list:
    print('There is a cat in my list')
else:
    print('There is no cat in my list')

#Task 7- Get the name of a Marvel character
print('\nTask 7')
marvel_name = input('What is a name of a Marvel character? ')
random_insert(marvel_name)

#Task 8- Get the index for the Marvel character and print it
print('\nTask 8')
print(marvel_name + ' is at index ' + str(user_list.index(marvel_name)))

#Task 9- Copy all the integers in the original list to a new list, then sort and print out that list
print('\nTask 9')
for i in user_list:
    try:
        int(i)
        int_list.append(int(i))
    except:
        continue

int_list.sort()
print('This is your list but only integers, sorted')
print(int_list)

#Task 10- Convert the original list to a tuple and print the tuple
print('\nTask 10')
tuple_time = tuple(user_list)
print(tuple_time)

#Task 11- Try and change the first item in the tuple
print('\nTask 11')
try:
    tuple_time[0] = 'cat'
except:
    print('Tuples are immutable!')

#Task 12- One last task
print('\nTask 12')
list_in_list = [[1,2,3],['a','b','c']]

for i in list_in_list:
    for j in i:
        print (j)

print()
print()
print('Press Enter to end the script')
input()
