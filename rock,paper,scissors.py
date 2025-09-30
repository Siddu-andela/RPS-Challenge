import random
choices=["rock","paper","scissors"]
print("Type 'rock','paper','scissors' to play.Type 'quit' if u want to exit.\n")
while True:
    player_choice=input("Enter your choice:").lower()
    if player_choice=="quit":
        print("Thanks for playing!bye")
        break
    if player_choice not in choices:
        print("please type rock,paper,or scissors only and you want to quit type quit\n")
        continue
    computer_choice=random.choice(choices)
    print(f"computer choice:{computer_choice}")
    if player_choice==computer_choice:
        print("Tie...\n")
    elif(player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!\n")
    else:
        print("You lose!\n")
