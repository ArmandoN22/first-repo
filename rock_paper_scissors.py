import random

def get_player_choice(options):
    while True:
        choice = input("Which hand are you going to choose? (rock - paper - scissors): ").lower()
        
        if choice not in options:
            print("Invalid OPtion. Try again")
            continue

        return choice
        break


def get_round_winner(computer_choice, player_choice):

    if player_choice == computer_choice:
        return "draw"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
            return "player"
    else:
        return "computer"

def play_game():

    options = ["rock","paper","scissors"]
    player_score = 0
    computer_score = 0

    while player_score != 2 and computer_score != 2:
        print("-------------------------------------------------------")

        computer_choice = random.choice(options)
        player_choice = get_player_choice(options)

        print(f'computer choice: {computer_choice}')
        print(f'player choice: {player_choice}')

        round_result = get_round_winner(computer_choice, player_choice)

        if round_result == "player":
            player_score += 1
            print("This round was won by the player")
        elif round_result == "computer":
            computer_score += 1
            print("this round was won by the computer")
        else: 
            print("This round was a draw")

    if player_score > computer_score:
        print(f'\n The winner is the player with {player_score} points.')
    else:
        print(f'\n the winner is the computer with {computer_score} points.')

def main():
    while True:

        play_game()
        again = input("\n Do you want to play again? Y/N: ").upper().strip()
        if again != "Y":
            print("Thanks for playing")
            break

if __name__ == "__main__":
    main()