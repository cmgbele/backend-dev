import random

users = {'Christopher':{'password':'qwertyuiop','high_score':0}} 
 
print('Welcome to this game')

while True:
    input_data= input('Enter l to login or s to signup.\n Enter any other key to quit.\n>').lower() 
    
    if input_data=='l':
        username = input('Username: ')
        password = input('Password: ')

        user = users.get(username)

        if user is not None and user['password'] == password:
            print('Enter H for help or any other key to continue')
            user_input = input('>').lower()

            help = """
            This is a simple terminal game where you have to guess a word and if your word is equal to the computer's choice, then you win

            Select from the given list of words"""

            if user_input == 'h':
                print(help)

            trial = 3
            scores = 0
            while trial >0:

                my_list = ['queen', 'jack', 'spades','king', 'love', 'ace']
                random.shuffle(my_list)
                print('\n', my_list)
                user_choice = input("\n Guess the word:\n").lower()
                computer = random.choice(my_list)

                if user_choice in my_list:

                    if user_choice==computer:
                        print("You Win!")
                        trial +=1
                        print(f'\n{trial} trial(s) left\n')

                        scores +=3
                        continue

                    else:
                        print(f'Computer selected {computer}')
                        print('Try again')

                else:
                    print('Invalid Input. Try again')
                    trial -=1
                    print(f'\n{trial} trial(s) left\n')

            if scores > user['high_score']:
                user['high_score'] = scores

        else:
            print('Please enter a valid username and password')
    
    elif input_data == 's':
        username1 = input('Username: ')
        password1 = input('Password: ')


        users[username] = {'password': password,'high_score': 0}

    else: 
        print('\nGood Bye')
        break

# with open("test.py", "w") as file:
#     file.write(f"{users}) 