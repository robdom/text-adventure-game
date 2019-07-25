# def start (hearts, shields, inventory):
#     been_here_before = False
#     if been_here_before == False:
#         hearts = 5
#         shields = 5
#         inventory = []

# # How do I pass the values of hearts, shields, and inventory to the next room function?

def room_0():
    print("You're in a cold dungeon lit by four flickering torches.")
    print("There are open doorways leading north, south, east and west.")
    print("Type n to go north. Type s to go south. Type e to go east. Type w to go west.")

    room_0_choice = input("> ")

    if room_0_choice == "n":
        room_1()
    elif room_0_choice == "s":
        room_4()
    elif room_0_choice == "e":
        room_3()
    elif room_0_choice == "w":
        room_2()
    else:
        print(">>> Please type n, s, e, or w. <<<")
        room_0()

def room_1():
    print("A giant spider is perched on its web in the corner.")
    print("Type 1 to attack the spider with your sword.")
    print("Type 2 to run north into the next room.")
    print("Type 3 to ask the spider a question.")
    print("Type 4 to back away from the spider.")

    room_1_choice = input("> ")

    if room_1_choice == "1":
        print("You kill the spider and earn a gold coin!")
        print("You head north into the next room.\n")
        room_5()
    elif room_1_choice == "2":
        print("Smart move. That spider could have killed you!\n")
        room_5()
    elif room_1_choice == "3":
        print("What question do you want to ask the spider?")

        spider_question = input("> ")

        print("The spider stares at you, then kills you with a blast of venom.")
    elif room_1_choice == "4":
        room_0()
    else:
        print(">>> Please type 1, 2, 3 or 4. <<<")
        room_1()

def room_2():
    # print(ghost_stunned)
    # ghost_stunned = False
    # if ghost_stunned:
    #     print("The room is empty. Head back to the room you came from.\n")
    #     room_0()
    print("A ghost suddenly appears in front of you.")
    print("Type 1 to attack the ghost with your sword.")
    print("Type 2 to stun the ghost with your boomerang.")
    print("Type 3 to run away from the ghost.")

    room_2_choice = input("> ")

    if room_2_choice == "1":
        print("Your sword goes right through the ghost.")
        print("The ghost touches you and you die immediately.")
    elif room_2_choice == "2":
        print("Nice job! Your boomerang stuns the ghost.")
        print("Head back to the room you came from.\n")
        room_0()
    elif room_2_choice == "3":
        room_0()
    else:
        print(">>> Please type 1, 2, or 3. <<<")
        room_2()

def room_3():
    print("The room is empty.")
    print("Head back to the room you came from.\n")
    room_0()

def room_4():
    print("A huge vampire bat flies toward you, wanting to sink its teeth into your neck.")
    print("Type 1 to attack the bat with your sword.")
    print("Type 2 to stun the bat with your boomerang.")
    print("Type 3 to bite the bat before it bites you.")
    print("Type 4 to ask the bat a question.")

    room_4_choice = input("> ")

    if room_4_choice == "1":
        print("The bat easily dodges your sword and bites your neck, killing you swiftly and painfully.")
    elif room_4_choice == "2":
        print("Your boomerang misses and the bat sinks its teeth into your neck, killing you immediately.")
    elif room_4_choice == "3":
        print("A curious choice.")
        print("As soon as you bite the bat, your body melts into a steaming puddle of blood.")
    elif room_4_choice == "4":
        print("What question do you want to ask the bat?")

        bat_question = input("> ")

        print("The bat stops and a puzzled look appears on its face.")
        print("Then the bat smiles.")
        print("It says, 'Finally! An enlightened human. You may pass.'\n")
        room_4A()
    else:
        print(">>> Please type 1, 2, 3 or 4. <<<")
        room_4()

def room_4A():
    print("Type w to head west. Type e to head east. Type n to return to the room you came from.")

    room_4A_choice = input("> ")

    if room_4A_choice == "w":
        room_6()
    elif room_4A_choice == "e":
        room_7()
    elif room_4A_choice == "n":
        room_0()
    else:
        print(">>> Please type w, e, or n. <<<")
        room_4A()

def room_5():
    print("You hear unsettling creepy voices singing.")
    print("The hairs on your neck stand up.")
    print("It's as if the voices are seeping into your bones.")
    print("The voices sing, 'You'll never get out...you'll never get out...'")

    print("Type n to head north. Type s to head south. Type w to head west. Type e to head east.")

    room_5_choice = input("> ")

    if room_5_choice == "n":
        room_15()
    elif room_5_choice == "s":
        room_1()
    elif room_5_choice == "w":
        room_12()
    elif room_5_choice == "e":
        room_14()

def room_6():
    print("An evil wizard materializes in front of you.")
    print("It shouts in a strange language and fires a spell from its magic wand.")
    print("Type 1 to dodge the spell. Type 2 to raise your shield to block the evil magic. Type 3 to run away from the wizard.")

    room_6_choice = input("> ")

    if room_6_choice == "1":
        print("You're not fast enough. The spell pulverizes you into a quivering mass of jelly.")
    elif room_6_choice == "2":
        print("The evil spell bounces off your shield and obliterates the wizard! Let's go!!!")
        room_6A()
    elif room_6_choice == "3":
        room_4A()
    else:
        print(">>> Please type 1, 2, or 3. <<<")
        room_6()

def room_6A():
    print("Type s to head south. Type e to return to the room you came from.")

    room_6A_choice = input("> ")

    if room_6A_choice == "s":
        room_8()
    elif room_6A_choice == "e":
        room_4A()
    else:
        print(">>> Please type s or e. <<<")
        room_6A()

def room_7():
    print("A massive, shimmering, otherworldly hand emerges from the far wall and glides towards you.")
    print("Type 1 to let the hand grab you. Type 2 to attack the hand with your sword.")
    print("Type 3 to give the hand a high-five. Type 4 to run back to the previous room.")

    room_7_choice = input("> ")

    if room_7_choice == "1":
        print("The hand closes around you and pulls you into the wall.\n")
        room_11()
    elif room_7_choice == "2":
        print("Your sword pierces the hand and it disappears with a pop!")
        print("Oh no!")
        print("There's another one!")
        room_7()
    elif room_7_choice == "3":
        print("The attempted high-five misses.")
        print("The hand closes around you and pulls you into the wall.\n")
        room_11()
    elif room_7_choice == "4":
        room_4A()
    else:
        print(">>> Please type 1, 2, 3, or 4. <<<")
        room_7()

def room_8():
    print("Another cold dungeon room.")
    print("Will you ever escape?")
    print("Type n to go north. Type s to go south. Type e to go east. Type w to go west.")

    room_8_choice = input("> ")

    if room_8_choice == "n":
        room_6()
    elif room_8_choice == "s":
        room_11()
    elif room_8_choice == "e":
        room_10()
    elif room_8_choice == "w":
        room_9()
    else:
        print(">>> Please type n, s, e, or w. <<<")
        room_8()

def room_9():
    print("A large blob shaped like a chocolate kiss scoots on the floor towards you.")
    print("Type 1 to run away. Type 2 to slash the blob with your sword.")
    print("Type 3 to hit the blob with your boomerang.")

    room_9_choice = input("> ")

    if room_9_choice == "1":
        room_8()
    elif room_9_choice == "2":
        print("The blob splats on your sword. That was easy!")
        print("Return to the previous room.\n")
        room_8()
    elif room_9_choice == "3":
        print("The blob swallows your boomerang, burps, then swallows you whole.")
    else:
        print(">>> Please type 1, 2, or 3. <<<")
        room_9()

def room_10():
    print("A five-square-meter cube glows and hums in the center of the room.")
    print("Type 1 to strike the cube with your sword.")
    print("Type 2 to push the cube to try and move it.")
    print("Type 3 to dance on top of the cube.")
    print("Type 4 to return to the previous room.")

    room_10_choice = input("> ")

    if room_10_choice == "1":
        print("Your sword clangs on the cube. The cube keeps glowing and humming.")
        room_10()
    elif room_10_choice == "2":
        print("A secret passageway opens underneath the cube!")
        room_14()
    elif room_10_choice == "3":
        print("You dance your funkiest dance moves.")
        print("Breakdancing.")
        print("Flossing.")
        print("Salsa-merengue.")
        print("Even the electric slide and the cha-cha slide.")
        print("Nothing happens.")
        room_10()
    elif room_10_choice == "4":
        room_8()
    else:
        print(">>> Please type 1, 2, 3 or 4. <<<")
        room_10()

def room_11():
    print("The room is empty.")
    print("However, there appears to be a word carved into the wall.")
    print("The word is 'avocado.'")
    print("Your stomach rumbles. You would like some guacamole.")
    print("Head north to the next room.\n")
    room_8()

def room_12():
    print("Three brown rabbits with pointy ears and curious whiskers bounce around the room.")
    print("Type 1 to shoot the rabbits with your bow and arrow.")
    print("Type 2 to stun the rabbits with your boomerang.")
    print("Type 3 to run away from the rabbits.")

    room_12_choice = input("> ")

    if room_12_choice == "1":
        print("You line up all three rabbits on the same line.")
        print("You launch your arrow...")
        print("It pierces all three rabbits - amazing aim!")
        print("Head back to the previous room.")
        room_5()
    elif room_12_choice == "2":
        print("Your boomerang clangs off the first rabbit.")
        print("Its whiskers twitch.")
        print("Then all three rabbits attack and eat your arms and legs.")
    elif room_12_choice == "3":
        room_5()
    else:
        print(">>> Please type 1, 2, or 3. <<<")
        room_12()

def room_14():
    print("A five-square-meter cube sits in the center of the room.")
    print("You push with all your might, but you can't budge it.")
    print("The next room looks depressingly familiar...\n")
    room_5()

def room_15():
    print("The door slams shut behind you. There's no way out.")
    print("Six sinister snakes slither over to you.")
    print("The head snake asks, 'What is the forbidden fruit of this fungeon?'")
    print("You ask, 'What's a fungeon?'")
    print("The head snake replies, 'It's a fun dungeon, of course! Aren't you having fun?'")
    print("The head snake repeats its question:")
    print("'What is the forbidden fruit of this fungeon?'\n")

    print("Type your answer. You have one chance. Spelling counts!")

    room_15_choice = input("> ").lower()

    if room_15_choice == "avocado":
        print("The head snake nods in approval.")
        print("'You may pass.'")
        print("The six snakes escort you to the last room.")
        room_16()
    else:
        print("The head snake looks at you sadly.")
        print("'I'm sorry, that's going to cost you.'")
        print("All six snakes sink their fangs into you.")
        print("The venom burns through your brain like a blowtorch.")
        print("Your last thought before dying: ")
        print("'I have a sudden craving for Mexican food...'")

def room_16():
    print("There is a golden pedestal in the center of the room.")
    print("On the pedestal is a mystical triangle and a beautiful heart.")
    print("'Let's goooooooo!!!', you shout.")
    print("A door opens, and sunlight streams in.")
    print("The outside world awaits you as you continue your journey.")
    print("Congratulations!\n")

room_0()

