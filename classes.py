import random
class PasswordList():
    '''Class stores passwords in a dictionary to later be accessed''' 
    
    def __init__(self):
        self.pass_list = {}

    def random_password(self, length):
        '''Creates a random password with length 'length' ''' 

        # Possible characters for the password to have 
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        special_char = ['!','@','#','$','%','&','*','?']
        letters = 'abcdefghijklmnopqrstuvwxyz'

        # Initializes a variable to store the password in
        password = ''

        # Makes sure the password contain at least one of each type of character 
        random_list = random.sample(range(1,5), 4)
        for num in random_list:
            if num == 1:
                password = password + random.choice(letters)
            elif num == 2:
                password = password + random.choice(letters).upper()
            elif num == 3:
                password = password + random.choice(special_char)
            elif num == 4:
                password = password + str(random.choice(numbers))

        # Fill in rest of password with random characters
        for char in range(length - 4):
            kind = random.choice(range(1,5))
            if kind == 1:
                password = password + random.choice(letters)
            elif kind == 2:
                password = password + random.choice(letters).upper()
            elif kind == 3:
                password = password + random.choice(special_char)
            elif kind == 4:
                password = password + str(random.choice(numbers))
                
        return password
    
    def add_password(self):
        '''Adds password name, username and password to dictionary.
        If input for password is a number, it generates a random password of that length'''
        
        #ask for password name, username and password (or generate new password)
        new_pass_name = input('\nWhat would you like to name this password as: ')
        new_pass_username = input('\nWhat is your username for this password: ')
        new_pass_pass = input('\nWhat is the password(type a number to generate a random password of that length): ')

        #check if we have to generate new password
        try:
            if type(int(new_pass_pass)) == int:
                new_pass_pass = self.random_password(int(new_pass_pass))
        except:
            pass

        #store password and username
        self.pass_list[new_pass_name] = {new_pass_username : new_pass_pass}
        print('\n')
        print(self.pass_list)

    def delete_password(self):
        '''Removes password from dictionary, input must be name of password'''
        
        password_to_remove = input('\nWhich item would you like to remove? ')
        del(self.pass_list[password_to_remove])
        
    def list_passwords(self):
        '''lists passwords neatly'''
        
        print('\nHere are your stored passwords: \n')
        for item in self.pass_list:
            print(str(item) + '\n' + str(self.pass_list[item]))
            print('\n')

    def menu(self):
        '''Opens a menu to interact with the password dictionary easily'''
        
        not_done = True
        while not_done:
            print('\nWhat would you like to do?')
            print('\n1. Show Password list')
            print('\n2. Add Password to list')
            print('\n3. Delete Password from list')
            print('\n4. Quit')
            menu_option = input('\nEnter the number for your option: ')

            if menu_option == '1':
                self.list_passwords()
            elif menu_option == '2':
                self.add_password()
            elif menu_option == '3':
                self.delete_password()
            elif menu_option == '4':
                not_done = False
            else:
                print('\nPlease pick a number from the option menu: ')