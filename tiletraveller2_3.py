import random
seed = int(input("Input seed: "))
random.seed(seed)
NORTH = 'n'
EAST = 'e'
SOUTH = 's'
WEST = 'w'
choicelist = [NORTH,EAST,SOUTH,WEST]
YES = "y"
NO = "n"
yesno = [YES,NO]
def move(direction, col, row):
    ''' Returns updated col, row given the direction '''
    if direction == NORTH:
        row += 1
    elif direction == SOUTH:
        row -= 1
    elif direction == EAST:
        col += 1
    elif direction == WEST:
        col -= 1
    return(col, row)    
def is_victory(col, row):
    ''' Return true if player is in the victory cell '''
    return col == 3 and row == 1 # (3,1)
def print_directions(directions_str):
    print("You can travel: ", end='')
    first = True
    for ch in directions_str:
        if not first:
            print(" or ", end='')
        if ch == NORTH:
            print("(N)orth", end='')
        elif ch == EAST:
            print("(E)ast", end='')
        elif ch == SOUTH:
            print("(S)outh", end='')
        elif ch == WEST:
            print("(W)est", end='')
        first = False
    print(".")
def find_directions(col, row):
    ''' Returns valid directions as a string given the supplied location '''
    if col == 1 and row == 1:   # (1,1)
        valid_directions = NORTH
    elif col == 1 and row == 2: # (1,2)
        valid_directions = NORTH+EAST+SOUTH
    elif col == 1 and row == 3: # (1,3)
        valid_directions = EAST+SOUTH
    elif col == 2 and row == 1: # (2,1)
        valid_directions = NORTH
    elif col == 2 and row == 2: # (2,2)
        valid_directions = SOUTH+WEST
    elif col == 2 and row == 3: # (2,3)
        valid_directions = EAST+WEST
    elif col == 3 and row == 2: # (3,2)
        valid_directions = NORTH+SOUTH
    elif col == 3 and row == 3: # (3,3)
        valid_directions = SOUTH+WEST
    return valid_directions
def play_one_move(col, row, valid_directions,nolever):
    ''' Plays one move of the game
        Return if victory has been obtained and updated col,row '''
    victory = False
    direction = random.choice(choicelist)
    print("Direction:",direction)
    direction = direction.lower()
    nolever = False
    if not direction in valid_directions:
        print("Not a valid direction!")
    else:
        col, row = move(direction, col, row)
        victory = is_victory(col, row)
        nolever = True
    return victory, col, row, nolever
def lever(col,row,coincount):
    coins = int(0)
    totalcoins = coincount
    if col==1 and row == 2:
        pull = random.choice(yesno)
        print("Pull a lever (y/n):",pull)
    elif col == 2 and row == 2:
        pull = random.choice(yesno)
        print("Pull a lever (y/n):",pull)
    elif col == 2 and row == 3:
        pull = random.choice(yesno)
        print("Pull a lever (y/n):",pull)
    elif col == 3 and row == 2:
        pull = random.choice(yesno)
        print("Pull a lever (y/n):",pull)
    else:
        return totalcoins
    if pull == "Y" or pull =="y":
        coins+=1
        totalcoins = int(coincount+coins)
        print("You received 1 coin, your total is now {}.".format(totalcoins))
        return totalcoins
    else:
        coins+=0
        return totalcoins
# The main program starts here
def main():
    victory = False
    row = 1
    col = 1
    coincount = 0
    moves = 0
    nolever = False
    while not victory:
        valid_directions = find_directions(col, row)
        print_directions(valid_directions)
        victory, col, row, nolever = play_one_move(col, row, valid_directions,nolever)
        if nolever:
            coincount =lever(col,row,coincount)
        else:
            pass
        moves +=1
    print("Victory! Total coins {}. Moves {}.".format(coincount,moves))
main()
while True:
    svar = input("Play again (y/n): ")
    if svar == "y":
        main()
    else:
        break