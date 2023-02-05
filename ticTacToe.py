'''Simple game of tic tac toe, did all of this on my own with very little google help'''

import random

def ticTacToe_vs_random():
    '''This function does the tic tac toe game but you are up against a random robot basicly copy paste
    from player v player one im confused on how its working but ill allow it'''

    #variables that cannnot be reset every iteration
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    invertedBoard = [['', '', ''], ['', '', ''], ['', '', '']]
    gameWon = False

    while gameWon != True:
        #Variables that need to be reset every iteration
        counter = 0
        counter2 = 0
        set = ''
        lineEnd = '|'
        randomTurn = False

        #take user input and make sure that the input is acceptable
        while True:
            print('your turn')
            userX = input('x = ')
            userY = input('y = ')
            #--did this to fix weird error--
            userX = int(userX)
            userY = int(userY)
            if userX < 0 and userY < 0:
                print('Please put positive nubmers')
            elif userX < 3 and userY < 3:
                print('\n')
                break
            else:
                print('Input does not work')
            
        #change both boards based on user input and random inputs
        if board[userY][userX] == '':
            board[userY][userX] = 'X'
            invertedBoard[userX][userY] = 'X'
        else:
            print('INVALID SPACE GO AGAIN')
        #random turn
        while randomTurn != True:
            randomX = random.randint(0, 2)
            randomY = random.randint(0, 2)
            if board[randomY][randomX] == '':
                board[randomY][randomX] = 'O'
                invertedBoard[randomX][randomY] = 'O'
                randomTurn = True

        #display board
        for line in board:
            for space in line:
                if counter2 >= 2:
                    lineEnd = ''
                    if space != '':
                        print(space, end=lineEnd)
                    elif space != 'X' or 'O':
                        print(' ', end=lineEnd)
                else:
                    lineEnd = '|'
                    if space != '':
                        print(space, end=lineEnd)
                    elif space != 'X' or 'O':
                        print(' ', end=lineEnd)
                counter2 += 1
            counter2 = 0
            counter += 1
            if counter >= 3:
                pass
            else:
                print('\n-----')
        print('\n')

        #-v-check to see if game is won-v-

        #checking rows
        for line in board:
            if line == ['X', 'X', 'X']:
                print('You won')
                gameWon = True
                break
            elif line == ['O', 'O', 'O']:
                print('You lost')
                gameWon = True
                break
        #checking columns through the inverted board
        for column in invertedBoard:
            if column == ['X', 'X', 'X']:
                print('You won')
                gameWon = True
                break
            elif column == ['O', 'O', 'O']:
                print('You lost')
                gameWon = True
                break
        #checking diagonals manualy bc idk an algorithm
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
            board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            print('Congrats you won')
            gameWon = True
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
            board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            print('You lost :(')
            gameWon = True

            

def ticTacToe_vs_self():
    '''The function for the tic tac toe game where two people play against each other'''

    #variables that cannnot be reset every iteration
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    invertedBoard = [['', '', ''], ['', '', ''], ['', '', '']]
    gameWon = False
    turn = 'X'

    while gameWon != True:
        #Variables that need to be reset every iteration
        counter = 0
        counter2 = 0
        set = ''
        lineEnd = '|'

        #take user input and make sure that the input is acceptable
        while True:
            if turn == 'X':
                print("X turn")
            if turn == 'O':
                print('O turn')
            userX = input('x = ')
            userY = input('y = ')
            #--did this to fix weird error--
            userX = int(userX)
            userY = int(userY)
            if userX < 0 and userY < 0:
                print('Please put positive nubmers')
            elif userX < 3 and userY < 3:
                print('\n')
                break
            else:
                print('Input does not work')
            
        #change both boards based on user input
        if turn == 'X' and board[userY][userX] == '':
            board[userY][userX] = 'X'
            invertedBoard[userX][userY] = 'X'
            turn = 'O'
        elif turn == 'O' and board[userY][userX] == '':
            board[userY][userX] = 'O'
            invertedBoard[userX][userY] = 'O'
            turn = 'X'
        else:
            print('INVALID SPACE GO AGAIN')

        #display board
        for line in board:
            for space in line:
                if counter2 >= 2:
                    lineEnd = ''
                    if space != '':
                        print(space, end=lineEnd)
                    elif space != 'X' or 'O':
                        print(' ', end=lineEnd)
                else:
                    lineEnd = '|'
                    if space != '':
                        print(space, end=lineEnd)
                    elif space != 'X' or 'O':
                        print(' ', end=lineEnd)
                counter2 += 1
            counter2 = 0
            counter += 1
            if counter >= 3:
                pass
            else:
                print('\n-----')
        print('\n')

        #check to see if game is won
        #checking rows
        for line in board:
            if line == ['X', 'X', 'X']:
                print('Congrats X won')
                gameWon = True
                break
            elif line == ['O', 'O', 'O']:
                print('Congrats O won')
                gameWon = True
                break
        #checking columns through the inverted board
        for column in invertedBoard:
            if column == ['X', 'X', 'X']:
                print('Congrats X won')
                gameWon = True
                break
            elif column == ['O', 'O', 'O']:
                print('Congrats O won')
                gameWon = True
                break
        #checking diagonals manualy bc idk an algorithm
        if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X' or \
            board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
            print('Congrats X won')
            gameWon = True
        elif board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O' or \
            board[2][0] == 'O' and board[1][1] == 'O' and board[0][2] == 'O':
            print('Congrats O won')
            gameWon = True

def main():    
    wantToPlay = False

    while wantToPlay != True:
        userInput = input('What mode do you want to play (ai or vs or done or help): ')
        if userInput == 'vs':
            ticTacToe_vs_self()
        elif userInput == 'ai':
            ticTacToe_vs_random()
        elif userInput == 'done':
            print('Thank you for playing')
            break
        elif userInput == 'help':
            print('Im suprised anyone besides me is using this but here we go. \n\
First off, when starting a game, anytype of mode, when x = or y =  shows up, those are the x and y coordinates. \n\
Second when playing the vs mode, it is a 1 v 1 and X and O go everyother time. \n\
Third when playing the ai mode the ai will go right after you and show up in the same time the square gets printed and you can go next')

main()