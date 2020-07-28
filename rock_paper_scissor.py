# HELL YEAH, I MADE IT.
# I'M AWESOME.
import random
def choice_to_number(choice_1):
    game_spot_1={
        'ROCK' : 1,
        'PAPER' : 2,
        'SCISSOR' : 3 
    }
    return game_spot_1[choice_1]
def number_to_choice(num_1):
    game_spot_2={
        1 : 'ROCK',
        2 : 'PAPER',
        3 : 'SCISSOR'
    }
    return game_spot_2[num_1]   

def computer_winning():
    computer_win={
        1 : 'Computer WINS !!!',
        2 : 'This round goes to the computer !!!',
        3 : 'You LOSE !!!'
    }
    n=random.choice([1,2,3])
    print(computer_win[n])
def human_winning():
    human_win={
        1 : 'You WON !!!',
        2 : 'This round goes to the user !!!',
        3 : 'Congratulations. You WON !!!'
    }
    n=random.choice([1,2,3])
    print(human_win[n])

print(''' Welcome to rock paper scissors.
      
      >>> Start
      
      >>> Help
      
      >>> Quit
      
      Just type in one of the three choices. :)
      ''')
game_choice = input("\nEnter what you want to do: ")
game_choice=game_choice.lower()
while game_choice != 'quit':
    if game_choice =='start':
        rounds=int(input("How many rounds do you wanna play this game: "))
        human_score = 0
        computer_score = 0
        for i in range(rounds):
            human_choice = input('''Enter your Choice: 
                                1. ROCK
                                2. PAPER
                                3. SCISSOR
                                ''')
            computer_choice = random.choice(['ROCK','PAPER','SCISSOR'])
            if human_choice.isnumeric():
                human_choice=int(human_choice)
                human_choice = number_to_choice(human_choice)
                print(f'You Chose "{human_choice}"')
                print(f'The Computer Chose "{computer_choice}"')
            else:
                human_choice=human_choice.upper()
                print(f'You Chose "{human_choice}"')
                print(f'The Computer Chose "{computer_choice}"')
            if human_choice=='ROCK' and computer_choice=='ROCK':
                print("Tie")
            elif human_choice=='PAPER' and computer_choice=='ROCK':
                human_winning()
                human_score = human_score + 1
            elif human_choice=='SCISSOR' and computer_choice=='ROCK':
                computer_winning()
                computer_score=computer_score+1
            elif human_choice=='ROCK' and computer_choice=='PAPER':
                computer_winning()
                computer_score=computer_score+1
            elif human_choice=='PAPER' and computer_choice=='PAPER':
                print("tie")
            elif human_choice=='SCISSOR' and computer_choice=='PAPER':
                human_winning()
                human_score=human_score+1
            elif human_choice=='ROCK' and computer_choice=='SCISSOR':
                human_winning()
                human_score=human_score+1
            elif human_choice=='PAPER' and computer_choice=='SCISSOR':
                computer_winning()
                computer_score=computer_score+1
            elif human_choice=='SCISSOR' and computer_choice=='SCISSOR':
                print("tie")
            else:
                print("WRONG INPUT !!!")
            
            print(f'\nYour Score = {human_score}')
            print(f"The Computer's Score = {computer_score}")
        if human_score > computer_score:
            print("\n\n\nYou are the winner of this round. Good Job !!!")
        else:
            print("\n\n\nSorry!!! The Computer wins this round")
    elif game_choice =='help':
        print('''
            Type start to Enter the game
            Then enter the number of rounds you want to play the game
            Enter your choice between rock, paper and scissor or enter the corresponding number. 
            That will work too :).
            ENJOY ('u') 
              ''')
    else:
        print('''
            You entered something the computer did't recognise.
              _       _
               \('_')/
                 |_|
                _/ \_
            The computer judges you ;p
              ''')
    game_choice = input("Enter what you want to do: ")
    game_choice=game_choice.lower()
