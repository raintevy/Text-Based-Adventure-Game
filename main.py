# Raingsey Tevy
# 03/20/2024
# This program is a text-based adventure game.
import time
import hangman
import slidingtilepuzzle
import trickquestions


def main():
    rooms, objects = read_file()
    roomLocations = convertTxtDic(rooms)
    objectLocations = convertTxtDic(objects)

    # main prompt when first starting the program
    print('You suddenly wake up in a cave after passing out')
    time.sleep(1)
    x = 0
    while x != 3:
        time.sleep(1)
        print('\ndrip')
        x += 1
    print("\nYou don't remember what happened, but you need to find a way out")
    time.sleep(3)

    # game loop and closes files
    main_menu(roomLocations, objectLocations)
    rooms.close()
    objects.close()


def main_menu(roomLocations, objectLocations):
    room_a_action, room_b_action, room_c_action, room_d_action, room_e_action, room_f_action, room_g_action = \
        print_action_choices()
    action = ''

    # player variables (purposely no named constants)
    playerRoom = 'A'
    playerPouch = []
    playerLife = 1
    playerScore = 0

    # item variables
    torch = 0
    potion = 0
    map = 0

    # game variables
    hangmanGame = 0
    slidingPuzzle = 0
    trickQuestion = 0

    # if the user wants to exit all they would have to do is press x
    while action != 'X':
        # Player is in room A
        if playerRoom == 'A':
            # prints score upon entering room
            print(f'\nScore: {playerScore}\n')
            print('You are in ' + roomLocations['A'])
            print('')

            # list of action choices
            print(room_a_action)
            print()

            # asks user what they would like to do
            action = input("What would you like to do? ").upper()
            if action == 'E':
                playerRoom = 'B'
            elif action == 'W':
                playerRoom = 'C'

            # first item the user can come across
            elif action == 'L':
                if torch == 0:
                    print('\nYou look around the room')
                    time.sleep(1)
                    print('You notice a skeleton in the corner of the room holding something')
                    time.sleep(1)
                    print(f"You walk closer, it's a {objectLocations['A']}\n")
                    candy = input('Would you like to pick it up ([Y] or [N])? ').upper()
                    if candy == 'Y':
                        playerPouch.append(objectLocations['A'])
                        time.sleep(0.5)
                        print(f'You picked up the {objectLocations["A"]} and stored it in your pouch.')
                        torch = 1
                        playerScore += 50
                        playerRoom = 'A2'
                    elif candy == 'N':
                        print('You walk away')
                        playerRoom = 'A2'
                elif torch == 1:
                    print(f"The skeleton in the corner is sad, because you stole it's {objectLocations['A']} :(")
                    playerRoom = 'A2'
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        elif playerRoom == 'A2':
            print(f'\nScore: {playerScore}\n')
            print(room_a_action)
            action = input("What would you like to do now? ").upper()
            if action == 'E':
                playerRoom = 'B'
            elif action == 'W':
                playerRoom = 'C'
            elif action == 'L':
                time.sleep(1)
                print("The skeleton in the corner is sad, because you stole it's torch :(")
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        # Player is in room B
        elif playerRoom == 'B':
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["B"]}')
            time.sleep(1.5)
            print('A shadowy figure appears from the dark and invites you to play his game')
            time.sleep(1.5)
            print(f'\n{room_b_action}')
            action = input("What would you like to do? ").upper()
            if action == 'W':
                playerRoom = 'A'
            elif action == 'S' and hangmanGame == 1:
                playerRoom = 'E'
            elif action == 'S' and hangmanGame == 0:
                print(f'\nPath is blocked, seems you have to play to continue')
            elif action == 'P' and hangmanGame == 0:
                won = hangman.main()
                if won:
                    playerScore += 100
                    print('Score: +100')
                    hangmanGame += 1
                    playerRoom = 'B2'
                else:
                    playerLife -= 1
                    print(f'Lives - 1'
                          f'\nCurrent Lives left: {playerLife}')
                    hangmanGame += 1
                    if playerLife <= 0:
                        print('You died')
                        break
            elif action == 'L':
                time.sleep(0.5)
                print('\nThe figure is waiting impatiently for your answer')
                time.sleep(1.5)
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        elif playerRoom == 'B2':
            print(f'\nScore: {playerScore}')
            print('The shadowy figure disperses, revealing a passage where he stood')
            print('\n[W] to go West\n[S] to go South\n[L] to look around'
                  '\n[I] to inspect pouch and use items\n[X] to exit')
            action = input("What would you like to do now? ").upper()
            if action == 'W':
                playerRoom = 'A'
            elif action == 'S':
                playerRoom = 'E'
            elif action == 'L':
                print("Nothing else is in this room")
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)

            elif action == '' or float(action) >= 0 or float(action) < 0:
                print(f'\n* Please input a letter')

            elif action == 'R':
                continue

            elif action == 'X':
                break

        # Player is in room C
        elif playerRoom == 'C':
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["C"]}')
            time.sleep(2)
            print('\nAcross from you is a puzzle placed on a pedestal')
            time.sleep(2)
            print('\nBeneath it is written:'
                  '\n"Many have tried, few have succeeded"'
                  '\nYou may proceed if you wish to, but your final score will be impacted')
            time.sleep(2)
            print()
            print(room_c_action)
            action = input("What would you like to do? ").upper()
            if action == 'E':
                playerRoom = 'A'
            elif action == 'S':
                playerRoom = 'D'
            elif action == 'L':
                print('\nMountains of piles of books are scattered around you')
                time.sleep(2)
                print('\nYou wonder how all these books got here')
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
            elif action == 'P' and slidingPuzzle == 0:
                won = slidingtilepuzzle.main()
                if won:
                    playerScore += 100
                    print('Score +100')
                    slidingPuzzle += 1
                    playerRoom = 'B2'
                else:
                    try:
                        playerLife -= 1
                        slidingPuzzle += 1
                        if playerLife <= 0:
                            print('You died')
                            break
                    except TypeError:
                        break
            elif action == 'P' and slidingPuzzle > 0:
                print('Cannot play anymore')
                playerRoom = 'C2'

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        elif playerRoom == 'C2':
            print(f'\nScore: {playerScore}')
            print('\n[E] to go East\n[S] to go South\n[L] to look around\n[R] to reveal score'
                  '\n[I] to inspect pouch\n[X] to exit')
            action = input("What would you like to do now? ").upper()
            if action == 'E':
                playerRoom = 'A'
            elif action == 'S':
                playerRoom = 'D'
            elif action == 'L':
                print("Nothing else is in this room")
            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        # Player is in room D
        elif playerRoom == 'D':
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["D"]}')
            time.sleep(1.5)
            print('Maps of areas unknown to the world can be found here')
            time.sleep(1.5)
            print()
            print(room_d_action)
            action = input("What would you like to do? ").upper()
            if action == 'N':
                playerRoom = 'C'
            elif action == 'E':
                playerRoom = 'F'
            elif action == 'L':
                if map == 0:
                    print('\nYou look around the room')
                    time.sleep(1)
                    print('You notice a chest with something inside')
                    time.sleep(1)
                    print(f"You walk closer, it's a {objectLocations['D']}\n")
                    m = input('Would you like to pick it up ([Y] or [N])? ').upper()
                    if m == 'Y':
                        playerPouch.append(str(objectLocations['D']))
                        time.sleep(0.5)
                        print(f'You picked up the {objectLocations["D"]} and stored it in your pouch.')
                        playerScore += 50
                        map = 1
                        playerRoom = 'D'
                    elif m == 'N':
                        print('You walk away')
                        playerRoom = 'D'
                elif map == 1:
                    print("Nothing left is in the room")
                    playerRoom = 'D'

            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
                playerRoom = 'D'

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')

        # Player is in room E
        elif playerRoom == 'E':
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["E"]}')
            time.sleep(1.5)
            print('Eyes in jars are lined on the shelves')
            time.sleep(1.5)
            print()
            print(room_e_action)
            action = input("What would you like to do? ").upper()
            if action == 'N':
                playerRoom = 'B2'
            elif action == 'W':
                playerRoom = 'F'
            elif action == 'L':
                if potion == 0:
                    print('\nYou look around the room')
                    time.sleep(1)
                    print('You notice a chest with something inside')
                    time.sleep(1)
                    print(f"You walk closer, it's a {objectLocations['E']}\n")
                    p = input('Would you like to steal it?(Y/N) ').upper()
                    if p == 'Y':
                        playerPouch.append(objectLocations['E'])
                        time.sleep(0.5)
                        print(f'You picked up the {objectLocations["E"]} and stored it in your pouch.')
                        playerScore += 50
                        potion = 1
                        playerRoom = 'E'
                    elif p == 'N':
                        print('You walk away')
                        playerRoom = 'E'
                elif potion == 1:
                    print("Nothing left is in the room")
                    playerRoom = 'E'

            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
                playerRoom = 'E'

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                      print(f'\n* Please input a letter')
                except ValueError:
                  print('\n* Please input one of the letters above')

        # Player is in room F
        elif playerRoom == 'F':
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["F"]}')
            time.sleep(2)
            print('\nA burly, overweight man with a round face approaches you.'
                  '\nHe is wearing a blue baseball cap turned backward,'
                  ' a grayish-green T-shirt with a question mark, brown pants, and sneakers.')
            time.sleep(3)
            print('\n"Sup dude", he says, "to pass you gotta answer these three questions"')
            time.sleep(1.5)
            print('\n"But if you get three wrong, I can not promise your safety bud"')
            print()
            print(room_f_action)
            action = input("What would you like to do? ").upper()
            if action == 'W':
                playerRoom = 'D'
            elif action == 'E':
                playerRoom = 'E'
            elif action == 'S':
                playerRoom = 'G'
            elif action == 'P' and trickQuestion == 0:
                wonTrick = trickquestions.play_game()
                if wonTrick == True:
                    print(f"\nCongrats! You received a {objectLocations['F']}")
                    playerPouch.append(objectLocations['F'])
                    playerScore += 100
                    trickQuestion += 1
                    playerRoom = 'F2'
                if wonTrick == False:
                    try:
                        playerLife -= 1
                        print(f"Lives left: {playerLife}")
                        if playerLife <= 0:
                            print("You died")
                            break
                    except TypeError:
                        break
            elif action == 'P' and trickQuestion > 0:
                print("You can't play anymore")

            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
                playerRoom = 'F'

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                  print('\n* Please input one of the letters above')

        elif playerRoom == 'F2':
            print('\n"Congrats dude", He says as he drifts away on a golf cart')
            time.sleep(1)
            print(f'\nScore: {playerScore}\n')
            print(f'You are in {roomLocations["F"]}')
            print()
            print(room_f_action)
            action = input("What would you like to do? ").upper()
            if action == 'W':
                playerRoom = 'D'
            elif action == 'E':
                playerRoom = 'E'
            elif action == 'S':
                playerRoom = 'G'
            elif action == 'P' and trickQuestion == 0:
                wonTrick = trickquestions.play_game()
                if wonTrick == True:
                    print(f"\nCongrats! You received a {objectLocations['F']}")
                    playerPouch.append(objectLocations['F'])
                    playerScore += 100
                    trickQuestion += 1
                    playerRoom = 'F2'
                if wonTrick == False:
                    try:
                        playerLife -= 1
                        print(f"Lives left: {playerLife}")
                        if playerLife <= 0:
                            print("You died")
                            break
                    except TypeError:
                        break
            elif action == 'P' and trickQuestion > 0:
                print("You can't play anymore")

            elif action == 'I':
                print(f'\nItems: {playerPouch}')
                playerLife = useItems(playerPouch, playerRoom, objectLocations, roomLocations)
                playerRoom = 'F'

            elif action == 'R':
                continue

            # input validation
            elif action == '':
                print(f'\n* Please input a letter')
            else:
                try:
                    if float(action) >= 0 or float(action) < 0:
                        print(f'\n* Please input a letter')
                except ValueError:
                    print('\n* Please input one of the letters above')


        # Player is in room G
        elif playerRoom == 'G' and objectLocations['F'] in playerPouch:
            print(f'\nYou are in {roomLocations["G"]}')
            print(f'\nScore: {playerScore}\n')
            time.sleep(2)
            print('A crowd of people have formed to cheer you on as you make your last step out of this dungeon')
            time.sleep(2)
            print('\nYou may rest now, Thanks for playing ┏(＾0＾)┛┗(＾0＾) ┓')
            time.sleep(1)
            break
        elif playerRoom == 'G' and objectLocations['E'] not in playerPouch:
            print("Door is locked")
            playerRoom = 'F'


# reads the text files given
def read_file():
    rooms = open('Data/rooms.txt', 'r')
    objects = open('Data/objects.txt', 'r')
    return rooms, objects


def print_room_desc(roomLocations):
    room_a_desc = (f'\nTo the east is {roomLocations["B"]}'
                   f'\nTo the west is {roomLocations["C"]}')
    room_b_desc = (f'\nTo the west {roomLocations["A"]}'
                   f'\nTo the south is {roomLocations["E"]}')
    room_c_desc = (f'\nTo the south is {roomLocations["D"]}\
                   \nTo the east is a {roomLocations["A"]}')
    room_d_desc = (f'\nTo the north is {roomLocations["C"]}'
                   f'\nTo the east is {roomLocations["F"]}')
    room_e_desc = (f'\nTo the north is {roomLocations["B"]}'
                   f'\nTo the west is {roomLocations["F"]}')
    room_f_desc = (f'\nTo the east is {roomLocations["E"]}'
                   f'\nTo the west is a {roomLocations["D"]}'
                   f'\nTo the south is a {roomLocations["G"]}')
    room_g_desc = '\nYou escaped the rooms'
    return room_a_desc, room_b_desc, room_c_desc, room_d_desc, room_e_desc, room_f_desc, room_g_desc


def print_action_choices():
    room_a_action = ('[E] to go East\n[W] to go West\n[L] to look around'
                     '\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_b_action = ('[W] to go West\n[S] to go South\n[P] to play hangman'
                     '\n[L] to look around\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_c_action = ('[E] to go East\n[S] to go South\n[P] to play sliding tile puzzle\n[L] to look around'
                     '\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_d_action = ('[N] to go North\n[E] to go East\n[L] to look around'
                     '\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_e_action = ('[N] to go North\n[W] to go West\n[L] to look around'
                     '\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_f_action = ('[E] to go East\n[W] to go West\n[S] to go South\n[P] to play the trick questions quiz'
                     '\n[I] to inspect pouch and use items\n[R] to reveal score\n[X] to exit')
    room_g_action = '[N] to go back North\n[R] to review score\n[X] to exit'
    return room_a_action, room_b_action, room_c_action, room_d_action, room_e_action, room_f_action, room_g_action


# converts the text files given into dictionaries (used rooms as variables, because that's what I started on)
def convertTxtDic(rooms):
    roomsList = []
    roomsDic = {}
    for line in rooms:
        roomlist = line.split('|')
        for item in roomlist:
            i = item.strip()
            roomsList.append(i)
    for i in range(0, len(roomsList), 2):
        roomsDic[roomsList[i+1]] = roomsList[i]
    return roomsDic


# functionality of the items
def useItems(playerPouch, playerRoom, objectLocations, roomLocations):
    room_a_desc, room_b_desc, room_c_desc, room_d_desc, room_e_desc, room_f_desc, room_g_desc \
        = print_room_desc(roomLocations)
    if len(playerPouch) > 0:
        use = input("Would you like to use your items?(Y/N) ").upper()
        while use != 'N':
            ask = input("Which item would you like to use? ")
            if ask == objectLocations['A'] and objectLocations['A'] in playerPouch:
                if playerRoom == 'A' or playerRoom == 'A2':
                    print(room_a_desc)
                elif playerRoom == 'B' or playerRoom == 'B2':
                    print(room_b_desc)
                elif playerRoom == 'C' or playerRoom == 'C2':
                    print(room_c_desc)
                elif playerRoom == 'D':
                    print(room_d_desc)
                elif playerRoom == 'E':
                    print(room_e_desc)
                elif playerRoom == 'F':
                    print(room_f_desc)
                elif playerRoom == 'g':
                    print(room_g_desc)
                use = input("Would you like to use another item?(Y/N) ").upper()
            elif ask == objectLocations['D'] and objectLocations['D'] in playerPouch:
                print(' ---     ---     ---'
                    '\n| C | - | A | - | B |'
                    '\n ---     ---     ---'
                    '\n  |               |'
                    '\n ---     ---     ---'
                    '\n| D | - | F | - | E |'
                    '\n ---     ---     ---'
                    '\n          |'
                    '\n         ---'
                    '\n        | G |'
                    '\n         ---')
                print(f'You are in room: {playerRoom}')
                use = input("Would you like to use another item?(Y/N) ").upper()
            elif ask == objectLocations['E'] and objectLocations['E'] in playerPouch:
                playerLife = 2
                print(f'Player life +1')
                print(f'Lives left: {playerLife}')
                playerPouch.remove(objectLocations['E'])
                return playerLife
            elif ask == objectLocations['F'] and objectLocations['F'] in playerPouch:
                print(f'\nGo south of room F to use item')
                use = input("Would you like to use another item?(Y/N) ").upper()
    else:
        print('No items available in pouch')


main()

# Test #1: Inputting ints and floats instead of letters
# Used to just repeat the prompt, changed it so that it tells you what is wrong now and then repeats the previous prompt

# Test #2: Inputting punctuations
# Outputs the prompt and asks the user to input one of the letters above instead of asking to input a letter

# Test #3: Inputting while the time.sleep line is working
# Program works, sometimes? Would be better if the user just waited till the prompt finishes

# Summary:
# I approached this by first, making a map of the amount of rooms I wanted and their general layout. Then I needed to
# find a way to have the player character move from room to room. I got stuck on moving back and forth between rooms,
# but I got some help from cs majors, and it turned out that the problem was very simple

# 1. I tested to make sure that the player could exit out of the program whenever they wanted to stop playing,
# and I found that a while loop did this very well

# 2. I tested to make sure each one of the items worked, and I'm VERY proud of the map especially,
# but the potion took the longest for me to figure out even though it should've been simple.
# The torch was the last item I made, because I was running out of ideas that weren't going to take hours to complete.

# 3. I tested the clarity of the instructions by having other people use the program on their own to see which areas
# I need to be clearer on

# 4. I tested that the time module worked and actually had an effect on the program, instead of doing nothing. I wanted
# to make sure the user had time to read the prompts as they come in and don't get overwhelmed.

# 5. I tested to make sure that once the objects were taken,
# they would be gone and either used or in the player's pouch

# What doesn't work as I'd like is that sometimes the map prints A2 or B2 instead of just A. I'd also like to shorten
# the code more if I had the time and energy. Also I want to put the games in it's own file if possible

# I learned so much about python's syntax and debugging, I tried to incorporate what we learned
# over the quarter as much as possible
# I would have to make some slight changes, but I do want to add this project to my professional portfolio
