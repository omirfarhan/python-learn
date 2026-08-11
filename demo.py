import random
options = ["rock", "paper", "scissors"]
def get_choice():
    player_choice = input("enter a choice (rock, paper, scissors): ")
    
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices

def check_win(player, computer): 
    print(f"you chose player{player}, Computer chose{computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! you win"
        else:
            return "paper cover rock! you lose"
    elif player =="paper":
        if computer == "rock":
            return "paper cover rock"
        else: 
            return "scissors cuts paper"
    elif player == "scissors":
        if computer == "paper":
            return "scissors cut papers"
        else:
            return "Rock smashes scissors"
        
choices = get_choice()
result = check_win(choices["player"], choices["computer"])       
print(result)