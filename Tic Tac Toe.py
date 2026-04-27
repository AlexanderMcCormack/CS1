def display_board(board):
    print(f'''         
1  {board[0][0]} | {board[0][1]} | {board[0][2]}
 ----------
2  {board[1][0]} | {board[1][1]} | {board[1][2]}   
 ----------          
3  {board[2][0]} | {board[2][1]} | {board[2][2]}   
                      ''')


def get_players_move(board, player):
        while True:
                row = int(input('enter row'))
                column = int(input('enter column'))
                board[row-1][column-1] = player

def check_winner(board):
    while True:
        if board[0][0] == 'x' and board[0][1] == 'x' and board[0][2] == 'x':
                print('x has won the game')
        elif board[0][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                print('o has won the game')

        elif board[1][0] == 'x' and board [1][1] == 'x' and board [1][2] == 'x':
                print('x has won the game')
        elif board[1][0] == 'o' and board [1][1] == 'o' and board [1][2] == 'o':
                print('o has won the game')

        elif board[2][0] == 'x' and board [2][1] == 'x' and board [2][2] == 'x':
                print('x has won the game')
        elif board[2][2] == 'o' and board [2][1] == 'o' and board [2][2] == 'o':
                print('o has won the game')

        elif board[0][0] == 'x' and board [1][0] == 'x' and board [2][0] == 'x':
                print('x has won the game')
        elif board[0][0] == 'o' and board [1][0] == 'o' and board [2][0] == 'o':
                print('o has won the game')

        elif board [0][1] == 'x' and board [1][1] == 'x' and board [2][1] == 'x':
                print('x has won the game')
        elif board [0][1] == 'o' and board [1][1] == 'o' and board [2][1] == 'o':
                print('o has won the game')

        elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                print('x has won the game')
        elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'x':
                print('o has won the game')

        elif board [0][0] == 'x' and board [1][1] == 'x' and board [2][2] == 'x':
                print('x has won the game')
        elif board [0][0] == 'o' and board [1][1] == 'o' and board [2][2] == 'o':
                print('o has won the game')

        elif board [2][0] == 'x' and board [1][1] == 'x' and board [0][2] == 'x':
                print('x has won the game')
        elif board [2][0] == 'o' and board [1][1] == 'o' and board [0][2] == 'o':
                print('o has won the game')

        elif board [0][2] == 'x' and board [1][2] == 'x' and board [2][2] == 'x':
                print('x has won the game')
        elif board [0][2] == 'o' and board [1][2] == 'o' and board [2][2] == 'o':
                print('o has won the game')
        else:
                return False
def check_tie(board):
       return '' not in board  
        
def main():
        print("welcome to Tic-Tac-Toe")
        board =  [[' ',' ',' '],
                  [' ',' ',' '],
                  [' ',' ',' ']]
        print (display_board(board))
        
main()