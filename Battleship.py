import time
import random

def display_board(board):
    print(f'''    1    2    3    4    5         
1  {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} 
 ----------
2  {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]}
 ----------          
3  {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]}
 ----------
4  {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} 
 ----------
5  {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} 
  ''')

def get_number():
  while True:
    try:
        num = int(input('Enter space 1 through 5: ')) - 1

        if num >= 0 and num <= 4:
          return num
        else:
          print('Please enter a number between 1 and 5')  
    except ValueError:
      print('Please enter a number')

def place_bot_ships(b_board):
  print('The bot is now choosing spots')
  time.sleep(1)
  print('...')
  
  for i in range(4):
    time.sleep(1)
    row = random.randint(0,4)
    column = random.randint(0,4)

    if b_board[row][column] != '🔷':
      continue
    b_board[row][column] = '🚢'
    display_board(b_board)
    time.sleep(1)
    
def place_player_ships(p_board):
  for i in range(4):
    row = get_number()
    column = get_number()

    if p_board[row][column] != '🔷':
      print('Space taken')
      continue
    p_board[row][column] = '🚢'
    display_board(p_board)


def bot_shot(p_board, p_display_board):
  while True:
    row = random.randint(0, 4)
    column = random.randint(0, 4)

    if p_display_board[row][column] != '🔷':
      continue

    if p_board[row][column] == '🚢':
      print('Bot got a hit!')
      p_display_board[row][column] = '💥'
    else:
      print('Bot missed')
      p_display_board[row][column] = '❌'

    display_board(p_display_board)
    break

def player_shot(b_board, b_display_board):
  while True:
    row = get_number()
    column = get_number()

    if b_display_board[row][column] != '🔷':
      print('You have already shot there!')
      continue

    if b_board[row][column] == '🚢':
      print('player got a hit!')
      b_display_board[row][column] = '💥'
      return True
    else:
      print('player missed')
      b_display_board[row][column] = '❌'
      return False


    
def main():
  p_board = [['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷']
              ]
  
  b_board = [['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷'],
              ['🔷','🔷','🔷','🔷','🔷']
              ]

  p_display_board = [['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷']
                      ]
  
  b_display_board = [['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷'],
                      ['🔷','🔷','🔷','🔷','🔷']
                      ]
  
  place_player_ships(p_board)
  place_bot_ships(b_board)
  player_ships_destroyed = 0
  bot_ships_destroyed = 0

  while player_ships_destroyed < 4 and bot_ships_destroyed < 4:
    player_success = player_shot(b_board, b_display_board)
    
    if player_success: 
      bot_ships_destroyed += 1
      

    bot_success = bot_shot(p_board, p_display_board)

    if bot_success: 
      player_ships_destroyed += 1
      
    if player_ships_destroyed == 4: 
      print("bot has won")
    if bot_ships_destroyed == 4:
      print("Congrats, You won!")
main()