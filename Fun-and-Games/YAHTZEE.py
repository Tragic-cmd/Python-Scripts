# This is an attempt at making a yahtzee game simulator

x = int(4)

# Need to roll x amount of dice getting a random value for each one 1/5

while(True):
    y = x - int(input("You have ", , "Dice available. ", "How many dice are you going to roll? (1 - 5)-->"))
    import random    
    # d = [] # Dice Rolls list used to record results

    for y in range(x+1):
        if y != 1:
            d = []
            # ("\n\nThe results...", random.randint(0,6), "\n")
            d.append(random.randint(0,6))
            y = y - 133
        print(d)