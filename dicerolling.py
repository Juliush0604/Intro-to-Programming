from random import randint

def roll(qty, sides=6):
    """Roll the specified number of dice. Can change how many sides the dice have"""
    
    # create an empty array
    dice = []
    # for each die we're rolling...
    for n in range(qty):
        # append a random number between 1 and the number of sides to the list of dice
        dice.append(randint(1, sides))
    
    # The line below is called a list comprehension, and it would replace lines 6-11 if you were using it
    # dice = [randint(1, sides) for n in range(qty)]

    # print the actual values of the dice
    print(dice)

    return dice

def check_successes(dice_list, success_on):
    """Check how many dice succeed"""

    # Running total of successful dice
    successes = 0

    # For loop to access each die in the list
    for die in dice_list:
        # Compare each die to the success value
        if die >= success_on:
            successes += 1
    
    # Print additional info
    print(f"successes: {successes}, failures: {len(dice_list) - successes}")
    
    # return the number of successes
    return successes


check_successes(roll(10), 3)