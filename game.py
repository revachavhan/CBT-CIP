# Rock Paper Scissors Game by [Your Name] 🎮

import random
import time

def show_intro():
    print("\n" + "="*55)
    print("      🎮 Welcome to Rock Paper Scissors! 🎮")
    print("="*55)
    print("Rules: Rock beats Scissors, Paper beats Rock, Scissors beats Paper.")
    print("Type 'quit' anytime to exit the game.")
    print("🤫 Secret: Type 'show' to see the computer's next move!\n")

def dramatic_countdown():
    for word in ["Rock...", "Paper...", "Scissors...", "Shoot!"]:
        print(word)
        time.sleep(0.5)

def random_taunt():
    taunts = [
        "💻 Hah! Too easy for me!",
        "💻 Better luck next time, human!",
        "💻 I'm just getting started 😎",
        "💻 Is that all you've got?",
        "💻 Oops! I did it again!"
    ]
    return random.choice(taunts)

def play_game():
    show_intro()
    moves = ['rock', 'paper', 'scissors']
    rounds_played = 0
    player_score = 0
    computer_score = 0

    while True:
        print("\n👉 Select your choice: Rock / Paper / Scissors")
        player_choice = input("Your move (or type 'quit' to exit): ").lower()

        if player_choice == 'quit':
            print("\n🎮 Game Over!")
            print(f"Total rounds played: {rounds_played}")
            print(f"Final Score - You: {player_score} | Computer: {computer_score}")
            if player_score > computer_score:
                print("🏆 You were the ultimate champion!")
            elif player_score < computer_score:
                print("💻 Computer took the crown this time!")
            else:
                print("🤝 It's a draw overall! Well played.")
            print("Thanks for playing, legend! ✌\n")
            break

        if player_choice == 'show':
            secret_move = random.choice(moves)
            print(f"🤫 Psst... Computer is about to pick: {secret_move.capitalize()}")
            continue

        if player_choice not in moves:
            print("⚠ Invalid choice, please choose Rock, Paper, or Scissors.")
            continue

        computer_choice = random.choice(moves)
        print(f"\nYou chose: {player_choice.capitalize()}")
        dramatic_countdown()
        print(f"Computer chose: {computer_choice.capitalize()}")

        rounds_played += 1

        # Determine the winner
        if player_choice == computer_choice:
            print("🤝 It's a tie this round!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("🎉 You win this round!")
            player_score += 1
        else:
            print("💻 Computer wins this round!")
            print(random_taunt())
            computer_score += 1

        # Show live score after each round
        print(f"📊 Current Score - You: {player_score} | Computer: {computer_score}")
        print("-" * 55)

if __name__ == "__main__":
    play_game()
