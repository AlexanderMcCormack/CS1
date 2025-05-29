import random

def add_entry(websites, usernames, passwords):
    website = input("Enter the name of a website: ")
    username = input("Enter username: ")
    password = input("Enter password (press 'g' to generate): ")
   
    if password.lower() == "g":
        password = generate_password()
    websites.append(website)
    usernames.append(username)
    passwords.append(password)
    print(f"The following entry has been added: {website} : {username} : {password}")
    '''
    Adds an entry to the parallel array of websites, usernames, and passwords
    Args:
        websites (str): the list of websites
        usernames (str): the list of usernames
        passwords (str): the list of passwords
    Returns:
        parallel array: newly added to array of websites, usernames, and passwords
    '''
def get_index(websites):
    while True:
        website = input("which website do you want")

        if website in websites:
            return websites.index(website)
        else:
            print("the website you requested has not been added yet")
    '''
    Create a function called get_index that takes the list of websites. This function should prompt the user for a website and return the index of that website in the given list of websites.
    Args:
        websites(str): asks user for website
    Returns:
        returns all the information on the website
    '''
def print_entry(website, username, password):
    print(f"your website is {website}, your username is {username}, You password is {password}")
    '''
    Create a function print_entry that takes three elements (a website, username, and password trio) and prints them neatly in an f-string. 
    Args:
        website(str): print website
        username(str): print username
        password(str): print password
    Returns:
    displays the website information neatly in an f'String
    '''
def change_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites[index] = input('Enter new website: ')
    index = get_index(usernames)
    usernames[index] = input('Enter new username: ')
    index = get_index(passwords)
    passwords[index] = input('enter new password: ')
    '''
    Allow the user to change websites, usernames, and passwords
    Args:
        websites(str): enter new website
        usernames(str): enter new username
        passwords(str): enter new password
    Returns:
    stores information in index
    '''
def delete_entry(websites, usernames, passwords):
    index = get_index(websites)
    websites.pop(index)
    index = get_index(usernames)
    usernames.pop(index)
    index = get_index(passwords)
    passwords.pop(index)
    '''
    Allows the user to delete websites, usernames, and passwords
    Args:
        websites(list): deletes website choosen by user 
        usernames(list): deletes username choosen by user
        passwords(list): deltes password choosen by user 
    Returns:
    removes information choosen by the user
    '''
def check_password(pwd, length, display):
    total = 0

    for char in pwd:
        if char in list('0123456789'):
            total += 1
        if char in list('~!@#$%^&*()-_=+?'):
            total += 1
        if char in list('abcdefghijklmnopqrstuvwxyz'):
            total += 1
        if char in list('abcdefghijklmnopqrstuvwxyz'.upper()):
            total += 1
        if len(pwd) >= length:
            total += 1
    if total > 3:
        if display:
            print (f"{pwd} is secure")
        return True
    else:
        if display:
            print (f"{pwd} is not secure")
        return False
'''
    checks the security of the password
    Args:
        pwd(str): what is in the password 
        legnth(str): how long is the password
        display(str): display to user
    Returns:
        tells user if there password is secure
    '''
def get_length():

    while True:
        try:
            length = int(input('Enter length: '))
            if length < 4:
                print ("enter length greater than 3")
                continue
            return length
        except ValueError:
            print ("please enter an integer")
'''
    retrieves the passwords legnth
    Args:
        passwords(str):set username legnth
    Returns:
    sets minimum legnth for passwords
    '''
def generate_password():
    length = get_length()
    while True:
        pwd = ''.join(random.sample(list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$%^&*_-'), length)) 
        if check_password(pwd, length, False):
            print(f'Generated password is {pwd}')
            return pwd
        '''
    generates a password at random from the list
    Args:
        passwords(str): generates a password
    Returns:
    returns the new generated password to user
    '''
def main():
    websites = []
    usernames = []
    passwords = []

    add_entry(websites, usernames, passwords)    

    while True:
        choice = input('''Which would you like to do? Enter "q" to quit. 
                       
1. Add an entry
2. Print an entry
3. Print all entries  
4. Change an entry
5. Delete an entry
6. Generate a password
7. Check a password 
8. leave code                  
                       
''')
        if choice == "q":
            exit()
        elif choice == "1":
            add_entry(websites, usernames, passwords)
        elif choice == "2":
            index = get_index(websites)
            print_entry(websites[index], usernames[index], passwords[index])
        elif choice == "3":
            for index in range(len(websites)):
                print_entry(websites[index], usernames[index], passwords[index])
        elif choice == "4":
            change_entry(websites, usernames, passwords)
        elif choice == "5":
            delete_entry(websites, usernames, passwords)
        elif choice == "6":
            pwd = generate_password()
            print(f'Your new password is {pwd}')
            change_pwd = input('Do you want to replace a password with generated one? y/n ')

        elif choice == "7":
            pwd = input('Enter password: ')
            length = get_length()
            check_password(pwd, length, True)
        elif choice == "8":
            exit()
        else:
            print("Invalid choice. Please try again.")
        
main()

    






  