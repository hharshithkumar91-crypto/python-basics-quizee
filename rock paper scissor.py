
import random
user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Type rock/paper/scissor or q to quit: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        print("Invalid choice. Please try again.")
        continue

    random_number = random.randint(0, 2)
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == computer_pick:
        print("It's a tie!")
    elif (user_input == "rock" and computer_pick == "scissor") or \
         (user_input == "paper" and computer_pick == "rock") or \
         (user_input == "scissor" and computer_pick == "paper"):
        print("You win!")
        user_wins += 1  
    else:
        print("Computer wins!")
        computer_wins += 1 
print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Thanks for playing!")
