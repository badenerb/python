#Baden Erb
#Mod 02 Homework

import random
import sys
import copy

card_count = 0

game_deck = []
card_deck = [['Ace of Spades', 'King of Spades', \
            'Queen of Spades', 'Jack of Spades', \
            '10 of Spades', '9 of Spades', \
            '8 of Spades', '7 of Spades', \
            '6 of Spades', '5 of Spades', \
            '4 of Spades', '3 of Spades', \
            '2 of Spades'], \
            ['Ace of Diamonds', 'King of Diamonds', \
            'Queen of Diamonds', 'Jack of Diamonds', \
            '10 of Diamonds', '9 of Diamonds', \
            '8 of Diamonds', '7 of Diamonds', \
            '6 of Diamonds', '5 of Diamonds', \
            '4 of Diamonds', '3 of Diamonds', \
            '2 of Diamonds'],\
            ['Ace of Clubs', 'King of Clubs', \
            'Queen of Clubs', 'Jack of Clubs', \
            '10 of Clubs', '9 of Clubs', \
            '8 of Clubs', '7 of Clubs', \
            '6 of Clubs', '5 of Clubs', \
            '4 of Clubs', '3 of Clubs', \
            '2 of Clubs'],\
            ['Ace of Hearts', 'King of Hearts', \
            'Queen of Hearts', 'Jack of Hearts', \
            '10 of Hearts', '9 of Hearts', \
            '8 of Hearts', '7 of Hearts', \
            '6 of Hearts', '5 of Hearts', \
            '4 of Hearts', '3 of Hearts', \
            '2 of Hearts']]

def get_card(num_cards):
    print()
    rando_suit = 2
    rando_card = 2
    for i in range(num_cards):
        if(int(len(game_deck))==0):
            print('Sorry all out of cards!')
        else:
            while(True):
                rando_suit = random.randint(0, int(len(game_deck)-1))
                if(int(len(game_deck[rando_suit]))==0):
                    del game_deck[rando_suit]
                    rando_suit = random.randint(0, int(len(game_deck)-1))
                else:
                    rando_suit = random.randint(0, int(len(game_deck)-1))
                    rando_card = random.randint(0,int(len(game_deck[rando_suit]))-1)
                    break
            print(str(game_deck[rando_suit][rando_card]))
            del game_deck[rando_suit][rando_card]
            if(int(len(game_deck[rando_suit]))==0):
                del game_deck[rando_suit]

game_deck = copy.deepcopy(card_deck)
print(str(len(game_deck[0])))
while (True):
    try:
        card_count = int(input('How many cards would you like to be dealt: '))
    except:
        print('Make sure you use a number!')
    get_card(card_count)
    end = input('\nHit the Enter key to draw again from this deck\nS to shuffle the deck and draw again\nQ to quit: ')
    if (end == 'S'):
        game_deck = copy.deepcopy(card_deck)
        print('\nYour cards have been shuffled!\n')
    elif (end == 'Q'):
        break
    
print()
print()
print('Press Enter to end the script')
input()

    
    
    
