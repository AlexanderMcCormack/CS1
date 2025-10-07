
def count_vowels(name):
    '''
    counts vowels in user input 
    Args:
        number of voewls(str): print number of vowels 
    Returns:
        number of vowels in a word: 
    '''
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    total = 0
    for char in name:
            if char in vowels:
             total += 1
    return total
'''
def get_names(fullname):

get users name
args:
    names(str): 3 word name
returns:
    users inputed name 


    names = []
    name = ''

    for letter in name:
        if letter == ' ':
            name += names
            name = ''
        else:
            name = name + letter
        name += names
    return names
'''
def get_initials(name):
    '''
    Takes a name and returns the initials
    Args:
        initials(str): returns users initials 
    Returns:
    initials :
    '''
    end_initials = ' '
    first = first_name(name)
    second = middle_name(name)
    third = last_name(name)
    #split input into first, last, and middle name
    first_initial = first[0]
    second_inital = second[0]
    third_initial = third[0]
    end_initials = (first_initial + second_inital + third_initial)
    return (upper(end_initials))

def is_palindrome(name):
        '''
    Takes a string and checks wether it is a palindrome
    Args:
        name check(str): checks if name is palindrome
    Returns:
        if string is palandrome : 
    '''
        return name == reverse_string(name) 


def reverse_string(name):    
    '''
    takes a string and reverses it 
    Args:
         return thing(str): user name 
    Returns:
        a reversed string : 
    '''
    reverse_name = str.lower(name[::-1])
    #returns name from back to front
    return(reverse_name)

def lower(name):
    '''
    takes a letter and changes it from uppercase to lowercase
    args:
        change uppercase letter(str): changes a letter to lowercase
    returns:
        lowercase letter
    '''
    name_out=""
    for letter in name:
        if ord(letter)>64 and ord(letter)<91:
            number=ord(letter)
            number=number + 32
            letter = chr(number)
            name_out +=letter
        else:
            name_out = name_out + letter
    return name_out
        
def upper(name):
    '''
    takes a letter and changes it from uppercase to lowercase
    args:
        change uppercase letter(str): changes a letter to lowercase
    returns:
        lowercase letter
    '''
    name_out=""
    for letter in name:
            if ord(letter)>96 and ord(letter)<122:
                number=ord(letter)
                number=number - 32
                letter = chr(number)
                name_out += letter
            else:
                name_out = name_out + letter
    return name_out
            
def first_name(name):
    names = name.split(" ")
    return names[0]

def last_name(name):
    names = name.split(" ")
    return names[2]

def middle_name(name):
    names = name.split(' ')
    return names [1]

def hyphen(name):

    hyphen = '-'
    if hyphen in name:
        print ("true")
    else:
        print ("false")
 
def main():
   
    '''
    Calls on all of the functions and allows the user to select which one they want to use
    Args:
       everything
    Returns:
    the functions
    '''

    name = input("What is your name ")

    while True:
        choice = input('''Which would you like to do? Enter "q" to quit. 
                    
        1. count vowels
        2. get initials 
        3. is palindrome 
        4. reverse string
        5. lowercase letters
        6. uppercase letters
        7. first name                 
        8. last name
        9. middle name
        10. hyphen 
        11. exit code              
                            
        ''')
        if choice == "1":
            print (count_vowels(name))
        elif choice == "2":
            print (get_initials(name))
        elif choice == "3":
            print (is_palindrome(name))
        elif choice == "4":
            print (reverse_string(name))
        elif choice == "5":
            print (lower(name))
        elif choice == "6":
            print (upper(name))
        elif choice == "7":
            print(first_name(name))
        elif choice == "8":
            print (middle_name(name))
        elif choice =="9":
            print(last_name(name))
        elif choice =="10":
            print(hyphen(name))
        elif choice == "q":
            exit()
        else:
            print("Invalid choice. Please try again.")
            
            
main()
            