
def count_vowels(name):
    '''
    counts vowels in user input 
    Args:
        number of voewls(str): print number of vowels 
    Returns:
        number of vowels in a word: 
    '''
    vowels = ["a", "e", "i", "o", "u"]
    total = 0
    for char in name:
            if char in vowels:
             total += 1
    return total


def get_initials(name):
    '''
    Takes a name and returns the initials
    Args:
        initials(str): returns users initials 
    Returns:
    initials :
    '''
    names = name.split(" ")
    initials = ""
     
    for n in names:
        initials += n[0].upper() + ". "
    return initials


def is_palindrome(name):
        '''
    Takes a string and checks whether it is a palindrome
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
         return thing(str): context
    Returns:
        a reversed string : 
    '''
    return name[::-1]


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
            else:
                name_out = name_out + letter
    return name_out
            
def first_name(name):
    output = ''
    for letter in name:
         if letter==" ":
              break
         else:
              output = output+letter
    return output

def last_name(name):
    output = ''
    for letter in name [::-1]:
        if letter == " ":
            break
        else:
               output = output + letter
    lastname = reverse_string(output)
    return lastname
             

def main():
   
    '''
    Calls on all of the functions and allows the user to select which one they want to use
    Args:
       everything
    Returns:
    the functions
    '''
    name = input("what is your name?")




    while True:
            choice = input('''Which would you like to do? Enter "q" to quit. 
        
    1. count vowels
    2. get initials 
    3. is palindrome 
    4. reverse string
    5. uppercase letters
    6. lowercase letters
    7. first name                 
    8. last name
    9.
    10.
    11. exit code              
                        
    ''')
            if choice == "1":
                output = count_vowels(name)
                print(output)

            elif choice == "2":
                get_initials(name)
                
            '''
            elif choice == "3":
                is_palindrome(name)
            elif choice == "4":
                reverse_string(name)
            elif choice == "5":
                lower(name)
            elif choice == "6":
                upper(name)
            elif choice == "7":
                first_name(name)
            elif choid == "8":
                last_name(name)
            elif choice == "q":
                exit()
            else:
                print("Invalid choice. Please try again.")
            '''
            
main()
            