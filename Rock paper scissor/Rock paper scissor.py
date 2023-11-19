#Variables
rock = 'rock'
paper = 'paper'
scissor = 'scissor'

#Players choose
player1_choose = input('Player 1 choose : rock , paper or scissor ? ')
player2_choose = input('Player 2 choose : rock , paper or scissor ? ')

#If tied choose agin
while player1_choose == player2_choose:
    if player1_choose == player2_choose:
        print('The game was tied , play again')
        player1_choose = input('Player 1 choose : rock , paper or scissor ? ')
        player2_choose = input('Player 2 choose : rock , paper or scissor ? ')

#The roles
if player1_choose == rock and player2_choose == scissor :
    print('Player 1 win!')

if player1_choose == rock and player2_choose == paper :
    print('Player 2 win!')

if player1_choose == paper and player2_choose == rock :
    print('Player 1 win!')


if player1_choose == paper and player2_choose == scissor :
    print('Player 2 win!')

    
if player1_choose == scissor and player2_choose == paper :
    print('Player 1 win!')


if player1_choose == scissor and player2_choose == rock :
    print('Player 2 win!')

