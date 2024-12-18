import random                                                                                                #import random

name = input ("what is your name")                                                                           #display message 
print ("goodluck", name)                                                                                     #display message 
rounds = 0                                                                                                   #set rounds to 0
correct = 0

while True:                                                                                                  #forevever loop
    number = random.randint(1, 10)                                                                           #set number to random number between 1 and 10
    print(number)
    guesses = 5                                                                                              #set number of guesses to 5 

    while guesses > 0:                                                                                       #while guesses are greater than 0
        while True:                                                                                          #forever loop
            guess = input ("the computer has chosen  number between 1 and 10, Guess the number")             #display message 

            try:
                guess = int(guess)                                                                           #attempt to convert guess to interger

                if guess >= 1 and guess <= 10:                                                               #if players guess is greater is greater that 1 and less than 10
                    break                                                                                    #end loop
                else:                                                                                        #else
                    print ("please enter a number between 1 and 10")                                         #display message 
            except ValueError:
                print ("please enter a number between 1 and 10")                                             #display message 

        if guess == number:                                                                                  #if player guess is equal to computer guess
            print ("you got it!")                                                                            #display message 
            correct += 1                                                                                     #add one to score
            break                                                                                            #end loop
        elif guess > number:                                                                                 #else if guess is greater than bot guess
            print ("your number is too high")                                                                #display message 
        else:                                                                                                #else if guess is less than bot guess
            print ("your number is too low")                                                                 #display message 

                                                                                                             #display message 
        guesses -= 1                                                                                         #add one to the guess amount 
    if guesses == 0:
        print ("you lost this round")
    rounds += 1
    
    while True:                                                                                              #forever loop 
        play_again = input (f"you got {correct} out of {rounds} rounds, would you like to play again yes/no? ")#display message of score and ask user if they want to play again
        if play_again == "no":                                                                               #if user says no
            exit()                                                                                           #end code
        elif play_again == "yes":                                                                            #else if user says yes 
            break                                                                                            #end forever loop
        else:                                                                                                #if user says anything else 
            print ("invalid response")                                                                       #display message 
