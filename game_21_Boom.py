import random
total_1: int = 0 #for the first calculation of the player's total.
total_2: int = 0 # reset a variable
total_player_1: int = 0 #memory cell and indicator for winning or losing
player_1_final: int = 0 #memory cell for the sum of the player card

#setting player number 1
for _ in range(1):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    player_1 = card_1
    if card_1 == "J" or card_1 == "Q" or card_1 == "K":
        card_1 = 10
    elif card_1 == "A":
        card_1 = 1

    card_2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A'])
    player = card_2
    if card_2 == "J" or card_2 == "Q" or card_2 == "K":
        card_2 = 10
    elif card_2 == "A":
        card_2 = 1

    print ("player 1 have: ", player_1, suit ,player, suit)
    total_1: int = card_1 + card_2
    player_1_final = total_1
    print ("your total is: ", total_1,'\n')
    choose = int(input("press 0 to stop"'\n' "press 1 to continue"'\n'))

    #getting another card
    if choose == 0:
        print ("you choose to stop🛑 your total is: ", total_1, '\n')

    if choose == 1:
            add_on = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
            player = add_on
            if add_on == "J" or add_on == "Q" or add_on == "K":
                add_on = 10
            elif add_on == "A":
                add_on = 1

            print ('\n'"you choose to continue, that is your add on card: ",add_on, suit)
            total_player_1 = total_1 + add_on
            player_1_final = total_player_1
            print ("your new total is: "'\n', total_player_1)

            #one last chance to win
            while total_player_1 < 21:
                Hit = int(input("would you like to Hit one last time?" '\n' "if so, press 1, if not, press 0: "'\n'))
                if Hit == 1:
                    last = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
                    total_2 = last
                    if last == "J" or last == "Q" or last == "K":
                        last = 10
                    elif last == "A":
                        last = 1
                    print("you choose to continue"'\n'"that is your last card: ", last, suit)
                    last_ = total_2 + total_player_1
                    player_1_final = last_
                    print("your new total is: "'\n', last_)
                    break
                if Hit == 0:
                    print ("you choose to stop" , '\n')
                    break

        #checking if it is a winner or a losser
            if total_player_1 == 21:
                print ("player 1, you win!🤩"'\n')

            elif total_player_1 > 21:
                print ("player 1, you lost!😔"'\n')

    #setting player number 2
total_1: int = 0 #reset the variable and for the first calculation of the player's total.
total_2: int = 0 # reset a variable
player_2_final: int = 0 #memory cell for the sum of the player card

for _ in range(1):
    suit = random.choice(["❤️", "♦️", "♣️", "♠️"])
    card_3 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
    player_2 = card_3
    if card_3 == "J" or card_3 == "Q" or card_3 == "K":
        card_3 = 10
    elif card_3 == "A":
        card_3 = 1

    card_4 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,'J', 'Q', 'K', 'A'])
    player__2 = card_4
    if card_4 == "J" or card_4 == "Q" or card_4 == "K":
        card_4 = 10
    elif card_4 == "A":
        card_4 = 1

    print ("player 2 have: ", player_2, suit ,player__2, suit)
    total_1: int = card_3 + card_4
    player_2_final = total_1
    print ("your total is: ", total_1,'\n')
    choose = int(input("press 0 to stop"'\n' "press 1 to continue"'\n'))

    #getting another card
    if choose == 0:
        print ("you choose to stop, your total is: ", total_1)

    if choose == 1:
            add_on = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
            player = add_on
            if add_on == "J" or add_on == "Q" or add_on == "K":
                add_on = 10
            elif add_on == "A":
                add_on = 1

            print ("you choose to continue, that is your add on card: ",add_on, suit)
            total_player_2 = total_1 + add_on
            player_2_final = total_player_2
            print ("your new total is: ", total_player_1)

            #one last chance to win
            while total_player_2 < 21:
                Hit = int(input("would you like to Hit one last time?" '\n' "if so, press 1, if not, press 0: "))
                if Hit == 1:
                    last = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'])
                    total_2 = last
                    if last == "J" or last == "Q" or last == "K":
                        last = 10
                    elif last == "A":
                        last = 1
                    print("you choose to continue, that is your last card: ", last, suit)
                    last_ = total_2 + total_player_1
                    player_2_final = last_
                    print("your new total is: ", last_)
                    break
                if Hit == 0:
                    print ("you choose to stop")
                    break

        #checking if it is a winner or a losser
            if total_player_2 == 21:
                print ("player 2, you win!🤩"'\n')

            elif total_player_2 > 21:
                print ("player 2, you lost!😔"'\n')


if player_1_final > player_2_final:
    print ("player 1 wins!🤩")
if player_2_final > player_1_final:
    print ("player 2 wins!🤩")
if player_1_final == player_2_final:
    print ("draw!😮")