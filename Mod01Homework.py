#Mod 01 Homework
#Baden Erb

import random
import sys

SODA_PRICE = 100
price_var = random.randint(-3,3) * 5
final_price = SODA_PRICE + price_var
total_input = 0
balance = final_price

print ('Welcome to the Soddie-Pop Shoppe. You can enter values of 5, 10, or 25 in payment.')
sodie_name = input('What sodie-pop do you want? ')
print('The current price for ' + sodie_name + ' is ' + str(final_price) + ' cents')

while(True):
    coin_input = input('What coin are you gonna insert? ')
    total_input += int(coin_input)
    balance = final_price - total_input
    if(balance > 0):
        print('You still owe ' + str(balance) + ' cents.')
    elif(balance < 0):
        print('You have been refunded ' + str(abs(balance)) + ' cents.')
        break
    else: 
        break

print('Enjoy your ' + sodie_name)
