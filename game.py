import random

choices = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
user_score = 0
computer_score = 0


def get_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'Tie'
    elif (user_choice == 'r' and computer_choice == 's') or \
            (user_choice == 's' and computer_choice == 'p') or \
            (user_choice == 'p' and computer_choice == 'r'):
        return 'User'
    else:
        return 'Computer'


def play():
    global user_score, computer_score
    user_choice = input("Enter your choice (r for rock / p for paper / s for scissors): ").lower()
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        return

    computer_choice = random.choice(list(choices.keys()))
    print(f"Computer chose: {choices[computer_choice]}")

    winner = get_winner(user_choice, computer_choice)
    if winner == 'Tie':
        print("It's a tie!")
    elif winner == 'User':
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1


def display_score():
    print("\nScore Card:")
    print(f"User: {user_score}")
    print(f"Computer: {computer_score}")


def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Play")
        print("2. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            play()
            display_score()
        elif choice == '2':
            display_score()
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
