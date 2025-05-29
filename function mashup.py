import random                                                                               #imports random variables

def chorus():                                                                               #defines chorus
    print ("Mary had a little lamb, little lamb, little lamb.")                             #print part of a song
    print ("Mary had a little lamb, its fleece was whiteas snow.")                          #print part of a song
def sing():                                                                                 #defines sing
    print ("And everywhere that Mary went. Mary went. Mary went.")                          #print part of a song
    print ("And everywhere that Mary went, the lamb was sure to go.")                       #print part of a song
    chorus()                                                                                #plays chorus
    print("It followed her to school one day, school one day, school one day.")             #print part of a song
    print("It followed her to school one day, which was against the rule.")                 #print part of a song
    chorus()                                                                                #plays chorus
    print("It made the children laugh and play, laugh and play, laugh and play.")           #print part of a song
    print("It made the children laugh and play to see the lamb at school.")                 #print part of a song
    chorus()                                                                                #plays chorus
    print("And so the teacher sent it out, sent it out, sent it out.")                      #print part of a song
    print("And so the teacher sent it out, but still it lingered near.")                    #print part of a song
    chorus()                                                                                #plays chorus
    print("It stood and waited round about, round about, round about.")                     #print part of a song
    print("It stood and waited round about, till Mary did appear.")                         #print part of a song
    chorus()                                                                                #plays chorus
    print("Why does the lamb love Mary so, Mary so, Mary so?")                              #print part of a song
    print("Why does the lamb love Mary so?” the little children cry.")                      #print part of a song
    chorus()                                                                                #plays chorus
def add (a, b):                                                                              
    '''
    adding two variables 
    Args:
        A, B (): context
    Returns:
        sum of a, b: 
    '''
    print(a + b)                                                                             

def print_list(the_list):                                                                   
        '''
    printing a list and choosing an element to print 
    Args:
        none (): context
    Returns:
        an element from the list: 
    '''
    for element in the_list:                                                                
        print (element)
        
def in_list(the_list, element):                                                              
    '''
    returns an element to the list 
    Args:
        none (): context
    Returns:
        an element to the list: 
    '''
    return element in the_list

def is_integer(number):                                                                     
    '''
   checks if input is an integer
    Args:
        somethings an integer (): context
    Returns:
        number of integers in input: 
    '''
    try:
        int(number)
        return True
    except ValueError:
        return False
    
def get_integers():
    '''
    asks user for two numbers 
    Args:
        if is integer is same as get integer (): context
    Returns:
        the numbers: 
    '''
    while True:
        number1 = input("enter number: ")
        number2 = input("enter new number: ")
        if is_integer (number1) and (number2):
            return int(number1), int(number2)
        
def get_random():
    '''
    chooses numbers from get integers
    Args:
        none (): context
    Returns:
        print number between a, b: 
    '''
    a, b = get_integers()
    print(random.randint(a, b))
    
def count_vowels(string):
    '''
    counts vowels in user input 
    Args:
        none (): context
    Returns:
        number of vowels in a word: 
    '''
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for char in string:
        if char in vowels:
            total += 1
    return total

def reverse_string(string):    
    '''
    takes a string and reverses it 
    Args:
        none (): context
    Returns:
        a reversed string : 
    '''
    return string[::-1]
    
def is_palindrome(string):
    '''
    Takes a string and checks whether it is a palindrome
    Args:
        none (): context
    Returns:
        if string is palandrome : 
    '''
    return string == reverse_string(string)
def get_initials(name):
    '''
    Takes a name and returns the initials
    Args:
        none (): context
    Returns:
    initials :
    '''
    names = name.split(" ")
    initials = ""
     
    for n in names:
        initials += n[0].upper() + ". "
    return initials

def replace_charecter(string, old, new):
    '''
    Takes a string, an old character, and a new character, and replaces every instance in the string of the old character with the new
    Args:
        none (): context
    Returns:
    word with a new and replaced charector:
    '''
    new_string = " "

    for char in string:
        if char == old:
            new_string =+ new
        else:
            new_string =+ char
    return new_string
        

def main():
    while True:
        option = input("What would you like to do? 1. Sing a song, 2. add two numbers, 3. take a list and print every element in the list, 4. Check if the element is in the list, 5. Check if input is an integer or not, 6. Gets you two integers, 7. gets two integers and picks a random number between them, 8. Get a string and take the number of vowels from the string, 9. Would you like to reverse a string, 10. Would you like to know if your name is a palindrome, 11. Would you like to get the initials of your name, 12. Would you like to replace characters in a word,")
        the_list = ["cow", "pig", "bird", "lamb", "human", "worm"]
        if option == "1": 
            sing()
        elif option == "2":
            add(1, 2)
        elif option == "3":
            print_list(the_list)
        elif option == "4":
            print(in_list(the_list,"pig"))
            print(in_list(the_list, "cow"))
        elif option == "5":
            print(is_integer('dog'))
            print(is_integer('5'))
        elif option == "6":
            a, b = get_integers()
            add(a, b)
        elif option == "7":
            get_random()
            word = input("Please enter a word or phrase: ")
        elif option == "8":
            print(count_vowels(word))
        elif option == "9":
            print(reverse_string(word))
        elif option == "10":
            print(is_palindrome(word))
        elif option == "11":
            name=input("Please enter a full name: ")
            print(get_initials(name))
        elif option == "12":
            text = input("Enter a word or phrase: ")
            old_character = input("Enter a letter to replace: ")
            new_character = input("Enter a letter that repleaes the old charcter ")
            print(repace_character(text, old_character, new_character))
      


main()



