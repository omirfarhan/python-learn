import random
options = ["rock", "paper", "scissors"]
def get_choice():
    player_choice = input("enter a choice (rock, paper, scissors): ")
    
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

a=11
choices = get_choice()
print(choices)


