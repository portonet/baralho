import random

suit_choices = ("Diamonds", "Hearts", "Clubs", "Spades")
suit_picked = random.choice(suit_choices)
cards_values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

card_picked = random.choice(cards_values)

if suit_picked == ("Diamonds") or ("Hearts"):
    suit_color = ("R")
elif suit_picked == ("Clubs") or ("Spades"):
    suit_color = ("B")
while True:
    guess=input("\nHello! Please, guess what is the color of the card. Type 'B' for 'black' or 'R' for 'red'")
    print("\nYou think the color is ", guess)
    
    
    print (suit_picked + card_picked + suit_color)
    # user_guess = ('\nEnter a suit to pick from. Your choices are listed above. ').title()

    if guess == suit_color:
        print ('\nYou guessed the correct suit color!')
        do_again = input('\nDo you want to try again? Y or N? ')
        if do_again == 'N':
            print ('\n See you later!')
            break
        else:
            print ('\nLets try it again.')
            continue
    else:
        print ('\nOooops')
        continue