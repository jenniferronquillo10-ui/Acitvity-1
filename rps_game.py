import random

choices = ["Rock", "Paper", "Scissor"]

while True:
    print(choices)
    Hello = input("Enter your choice (write 'quit' to quit): ").capitalize()

    if Hello == "Quit":
        print("Game Over")
        break

    if Hello not in choices:
        print("Invalid Choice")
        continue

    computer_choice = random.choice(choices)

    if Hello == computer_choice:
        print(f"{Hello} vs. {computer_choice} = It's a Tie")

    elif (
        (Hello == "Rock" and computer_choice == "Scissor") or
        (Hello == "Paper" and computer_choice == "Rock") or
        (Hello == "Scissor" and computer_choice == "Paper")
    ):
        print(f"{Hello} vs. {computer_choice} = You Win!")

    else:
        print(f"{Hello} vs. {computer_choice} = Computer Wins!")





