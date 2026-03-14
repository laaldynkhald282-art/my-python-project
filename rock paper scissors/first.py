import random

# save ascii in vairable
rock_ascii = """
    ___
---'   ____)
      (_)
      (_)
      (____)
---.(_)
"""

paper_ascii = """
     ___
---'    __)__
           __)
          ___)
         ___)
---.__)
"""

scissors_ascii = """
    ___
---'   __)__
          __)
       __)
      (____)
---.(_)
"""

print("Welcome to rock, paper, scissors game:")
confirm = input("press enter to continue or type (help) for the rules help\n").lower()

if confirm == "help":
    print("** rules **")
    print("1) you choose and computer choose")
    print("2) rock smashes scissors")
    print("3) paper covers rock")
    print("4) scissors beat paper")
    print("*******")

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

if user_choice not in ["rock", "paper", "scissors"]:
    print("invalid choice. please run the program again and choose rock, paper, scissors.")
else:
    # display user choice in ascii
    if user_choice == "rock":
        print(f"\nyou chose:\n{rock_ascii}")
    elif user_choice == "paper":
        print(f"\nyou chose:\n{paper_ascii}")
    else:
        print(f"\nyou chose:\n{scissors_ascii}")

    # computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    
    if computer_choice == "rock":
        print(f"computer chose:\n{rock_ascii}")
    elif computer_choice == "paper":
        print(f"computer chose:\n{paper_ascii}")
    else:
        print(f"computer chose:\n{scissors_ascii}")

    # determine the winner
    if user_choice == computer_choice:
        print("it's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print(f"you win! {user_choice} beats {computer_choice}.")
    else:
        print(f"you lose! {computer_choice} beats {user_choice}")