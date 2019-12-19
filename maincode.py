import numpy as np

#prints the board values
def printBoard(vals):
    for j in range(3):
        print("| ", end="")
        for i in range(3):
            print(vals[j][i], end=" ")
            print("|", end=" ")
        print("")
        print("")


#checks if the game is won
def checkVictory(vals):
    game_over = False
    #checks for row or column victories
    for i in range(3):
        if vals[0][i] == vals[1][i] and vals[1][i] == vals[2][i]:
            game_over = True
            return game_over
        elif vals[i][0] == vals[i][1] and vals[i][1] == vals[i][2]:
            game_over = True
            return game_over

    #checks for diagonal victories
    if vals[0][0] == vals[1][1] and vals[1][1] == vals[2][2]:
        game_over = True
        return game_over
    elif vals[2][0] == vals[1][1] and vals[1][1] == vals[0][2]:
        game_over = True
        return game_over
    return game_over


def checkCatGame(vals):
    cat_game = True
    #checks for cat game
    for x in range(1, 10):
        if np.isin(str(x), vals):
            cat_game = False
    game_over = cat_game
    return cat_game


#prompts for move input, if the move can be made, vals is changed
def makeMove(player, vals):
    not_ok_move = True
    print("it is player", player, "'s turn.")
    while not_ok_move:
        move = input("what move do you want? ")
        if np.isin(str(move), vals):
            not_ok_move = False

    for x in range(3):
        for y in range(3):
            if vals[x][y] == move:
                vals[x][y] = player
                break


#main functionality
print("Welcome to Tic Tac Toe!")
vals = np.array(['1', '2', '3', '4', '5', '6', '7', '8', '9']).reshape(3, 3)
player = 'X'

game_over = False
#continue prompting for new moves until the game is over
while game_over == False:
    printBoard(vals)
    makeMove(player, vals)
    printBoard(vals)
    if checkCatGame(vals) or checkVictory(vals):
        game_over = True
        break
    #switch players
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

if checkCatGame(vals):
    print("Cat game!")
else:
    print(player, "won the game")
print("thanks for playing!")
