import random

def get_user_choice():
    """Prompt the user to choose rock, paper, or scissors."""
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice (rock, paper, or scissors) for the computer."""
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's choice and the computer's choice."""
    if user_choice == computer_choice:
        return 'tie'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return 'user'
    else:
        return 'computer'

def display_result(user_choice, computer_choice, winner):
    """Display the user's choice, computer's choice, and the result of the game."""
    print(f'Your choice: {user_choice}')
    print(f'Computer\'s choice: {computer_choice}')
    if winner == 'tie':
        print('It\'s a tie!')
    elif winner == 'user':
        print('You win!')
    else:
        print('Computer wins!')

def play_game():
    """Play one round of the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)
    display_result(user_choice, computer_choice, winner)
    return winner

def main():
    user_score = 0
    computer_score = 0

    while True:
        winner = play_game()
        if winner == 'user':
            user_score += 1
        elif winner == 'computer':
            computer_score += 1

        print(f'Score - You: {user_score}, Computer: {computer_score}')

        play_again = input('Do you want to play again? (yes/no): ').lower()
        if play_again != 'yes':
            print('Thanks for playing! Goodbye!')
            break

if __name__ == "__main__":
    main()
