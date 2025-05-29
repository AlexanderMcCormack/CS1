"author, Alexander McCormack"
"date, 4/4/25"
"description, This game allows you to order some food and it calculates the total price, I did 4 challenges"


import random                                                                                                                   #import random
mains = ["broccoli", "steak", "potatoes", "spaghetti", "pizza", "bread sticks", "salmon", "chicken", "rice"]                     #list of main foods
prices = [15, 45, 12, 30, 25, 8, 43, 40, 25]                                                                                    #list of main food prices
flairs = ["butter", "tequila", "garlic butter", "red wine", "buffalo dipping sauce", "olive oil", "teriyaki", "garlic", "salt"] #list of flairs
flair_prices = [3, 20, 5, 25, 6, 2, 7, 1, 1]                                                                                    #list of flair prices


while True:                                                                                                                     #forever loop
    try:                                                                                                                        #attempt block of code
        items = int(input("how many items do you want"))                                                                        #ask user how many items they want
    except ValueError:                                                                                                          #if user enters invalid statement 
        print('Please enter an integer')                                                                                        #display message
        continue                                                                                                                #restarts code

    total = 0                                                                                                                   #total cost is 0
   
    for i in range(items):                                                                                                      #do things in the list
        main = random.choice(mains)                                                                                             #choose a radnom item from list mains
        flair = random.choice(flairs)                                                                                           #choose random item from list flairs
        price = prices[main.index(main)]                                                                                        #choose random from prices
        flair_price = flair_prices[flairs.index(flair)]                                                                         #choose random for flair prices
        total += price + flair_price                                                                                            #add up the price and flair price
        print(f'{main} with {flair}, Your cost is ${price} + ${flair_price} = ${price+flair_price}')                            #display the outputs
                            
    print(total)                                                                                                                #print total price

    
