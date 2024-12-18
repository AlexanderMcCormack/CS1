import random                                                                                   #import random
options = ["rock", "paper", "scissors","sword"]                                                 #list
score_limit = 5                                                                                 #set score limit to 5
score = 0                                                                                       #set score to 0
#cat
while True:
    choice = input('which game, magic 8 ball or rock paper scissors')                           #display message
    if choice == 'rock paper scissors':                                                         #if user choice is rock paper scissors
        while score < score_limit:                                                              #loop until limit reached
            user_choice = input ("rock, paper, scissors, or sword? ")                           #ask user question
            bot_choice = random.choice(options)                                                 #bot chooses random from list
            print(f"user chose {user_choice} and bot chose {bot_choice}")                       #display message
            if user_choice == "rock" and bot_choice == "paper":                                 #If user chooses rock and bot chooses paper 
                print("bot wins")                                                               #display message
                score -= 1                                                                      #-1 score
                print("Your current score is", score)                                           #display message                                                                                    
            elif user_choice == "rock" and bot_choice == "scissors":                            #If user chooses rock and bot chooses scissors 
                print("user wins")                                                              #display message
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message       
            elif user_choice == "rock" and bot_choice == "sword":                               #If user chooses rock and bot chooses sword
                print ("bot wins")                                                              #display message
                score -= 1                                                                      #-1 score                                                            #+
                print("Your current score is", score)                                           #display message                                                             #+1 score
            elif user_choice == "paper" and bot_choice == "scissors":                           #If user chooses paper and bot chooses scissors 
                print("bot wins")                                                               #display message
                score -= 1                                                                      #-1 score
                print("Your current score is", score)                                           #display message       
            elif user_choice == "paper" and bot_choice == "rock":                               #If user chooses paper and bot chooses rock 
                print("user wins")                                                              #display message 
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message
            elif user_choice == "paper" and bot_choice == "sword":                              #If user chooses paper and bot chooses sword
                print ("bot wins")                                                              #display message
                score -= 1                                                                      #-1 score
                print("Your current score is", score)                                           #display message                                                                      #+1 score
            elif user_choice == "scissors" and bot_choice == "rock":                            #If user chooses scissors and bot chooses rock 
                print("bot wins")                                                               #display message
                score -= 1                                                                      #-1 score
                print("Your current score is", score)                                           #display message  
            elif user_choice == "scissors" and bot_choice == "paper":                           #If user chooses scissors and bot chooses paper
                print ("user wins")                                                             #display message
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message
            elif user_choice == "scissors" and bot_choice == "sword":                           #If user chooses scissors and bot chooses sword
                print ("bot wins")                                                              #display message
                score -= 1                                                                      #-1 score
                print("Your current score is", score)                                           #display message 
            elif user_choice == "sword" and bot_choice == "rock":                               #If user chooses sword and bot chooses rock
                print("user wins")                                                              #display message
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message 
            elif user_choice == "sword" and bot_choice == "paper":                              #If user chooses sword and bot chooses paper
                print ("user wins")                                                             #display message
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message #+1 score 
            elif user_choice == "sword" and bot_choice == "scissors":                           #If user chooses sword and bot chooses scissors 
                print ("user wins")                                                             #display message
                score += 1                                                                      #+1 score
                print("Your current score is", score)                                           #display message#display messagewhile True:                                                                             #forever loop
            elif user_choice == bot_choice:                                                     #if user and bot choose same thing
                print ("tie, try again")                                                        #display message
                                                                                
        if score == score_limit:                                                                #if score limit reached 
                print (""" ____      ____  _____  ____  _____  ____  _____  ___  
        |_  _|    |_  _||_   _||_   \|_   _||_   \|_   _||_   __  ||_   __ \   | |              
          \ \  /\  / /    | |    |   \ | |    |   \ | |    | |_ \_|  | |__) |  | | 
           \ \/  \/ /     | |    | |\ \| |    | |\ \| |    |  _| _   |  __ /   | | 
            \  /\  /     _| |_  _| |_\   |_  _| |_\   |_  _| |__/ | _| |  \ \_ |_| 
             \/  \/     |_____||_____|\____||_____|\____||________||____| |___|(_)""")          #display message 
                break                                                                           #end loop
                                                                              

                                                                               
    
    elif choice == 'magic 8 ball':                                                              #if user choise is 8 ball
        Question_markings = ["who", "what", "when", "where", "which", "how", "will", "am", "is"]#list
        while True:                                                                             #forever loop
            question = input("state your question")                                             #ask user question
        
            first_word = question.split()[0]                                                    #split question
            if first_word in Question_markings:                                                 #if detect words
                result = ["yes", "no", "maybe", "ask again later"]                              #list
                result =random.choice(result)                                                   #choose a random choice
                print(result)                                                                   #display message 
            else:                                                                               #else 
                print("no question asked")                                                      #display message 
    
    
