name = input('How would you like to be addressed by? ')
Welcome_Message = (f'Welcome to my first app, {name}!')
print(Welcome_Message)
secret_number = 5
guess_number = int(input('Guess the chosen secret number! '))
if guess_number == secret_number:
    print(f'Brraavooo {name}')
else:
    print(f"Aww. Sorry {name}, that's wrong. Try again.")