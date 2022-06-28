#!/usr/bin/env python

import random

def main():
    """ Learning Alphabet with Game !."""
    print("Guess that fruit!")

    print("\nEASY: You will be given an alphabet and you have to guess the fruit that start with that alphabet ")

    print( "\nPlease Start writing your answer with a CAPITAL letter" )

    fruit = [
        "cranberry",
        "cherry",
        "coconut",
        "Coconut",
        "Cranberry",
        "Coconut"
       ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("\nState a fruit that start with alphabet C ? "))
        
        if x == guess:
            print("You guessed {}. Cheers !! Correct!\U0001F601".format(guess))
            break
        else:
            print("You guessed {}. Oh No!. Try Again!\U0001F605".format(guess))


    fruit = [
        "Apple",
        "Avocado",
        "Apricot",
        "apricot",
        "avocado",
        "apple"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet A ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F602".format(guess))
            break
        else:
            print("You guessed {}. Haiyaa~!. Try Again!\U0001F600".format(guess))

    fruit = [
        "Banana",
        "Blueberry",
        "Blackcurrent",
        "banana",
        "blueberry",
        "blackcurrent"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet B ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F607".format(guess))
            break
        else:
            print("You guessed {}. We Can Do This! Another One \U0001F923".format(guess))

    fruit = [
        "Dragonfruit",
        "Durian",
        "Date"
        "dragonfruit",
        "durian",
        "date"]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet D ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct!\U0001F60D".format(guess))
            break
        else:
            print("You guessed {}. Never Give Up!. Try Again!".format(guess))

    fruit = [
        "Mango",
        "Mangosteen",
        "Melon",
        "mango",
        "mangosteen",
        "melon"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("State a fruit that start with alphabet M ? "))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct! \U0001F601".format(guess))
            break
        else:
            print("You guessed {}. Come On! !\U0001F612".format(guess))

    fruit = [
        "grape",
        "blackcurrent",
        "dragonfruit"
        ]

    x = random.choice(fruit)
    
    guess = None

    while x != guess:

        guess = str(input("MEDIUM: Guess a fruit that colored purple? \0001F619"))
        
        if x == guess:
            print("You guessed {}. Hurray! Correct! \U0001F601".format(guess))
            break
        else:
            print("You guessed {}. Come On! !\U0001F612".format(guess))

fruit = [
        "Contain pottasium",]

    x = random.choice(fruit)
    print("Choose the correct answer below")
    print("\nANSWERS OPTIONS: Contain Pottasium, Contain Zinc, Good For Digestion")
    print("\nPlease write the answer exactly like the answers options")
    
    guess = None

    while x != guess:

            guess = str(input("HARD: State the benefit for eating banana? \0001F619"))
            
            if x == guess:
                print("\nYou guessed {}. Hurray! Correct! \U0001F601".format(guess))
                break
            else:
                print("\nYou guessed {}. Come On! !\U0001F612".format(guess))

    


        

main()
       

