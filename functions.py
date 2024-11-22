def display_passwords(pass_list):
    # Count passwords in pass_list
    counter = 0

    # Get each item from the dictionary of passwords (site, username, password)
    for item in pass_list:
        site = str(item)
        
        for user in pass_list[item]:
            username = str(user)
            password = str(pass_list[item][user])
            counter += 1 

        # Print each password 
        print('Password #' + str(counter))
        print('Site: ' + site)
        print('Username: ' + username)
        print('Password: ' + password)
        print()


def encoder(pass_list):
    # Initialize variables to keep the decoded and encoded strings of passwords
    decoded = ''
    encoded = ''

    # Get each item in the dictionary of passwords
    for item in pass_list:
        site = str(item)
        decoded = decoded + site
        for user in pass_list[item]:
            username = str(user)
            password = str(pass_list[item][user])
            decoded = decoded + ' ' + username + ' ' + password + ' ' 

    # Encode each char in the string 
    for char in decoded:
        encoded_char = chr(ord(char) + 200)
        encoded = encoded + encoded_char

    return encoded


def decoder(encoded_string):
    # Initialize a variable to store decoded string
    decoded = ''
    
    # Decode each char in the encoded string
    for char in encoded_string:
        decoded_char = chr(ord(char) - 200)
        decoded = decoded + decoded_char

    # Split the string to get each item 
    decoded = decoded.split(' ')

    # Print each item neatly
    for item in decoded:
        print(item)

    
    


            

