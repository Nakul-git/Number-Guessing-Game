import random

def play_game():
    print("🎯 Welcome to The Perfect Guess Game!")
    
    # Generate random number
    number = random.randint(1, 100)
    guesses = 0

    while True:
        try:
            user_input = int(input("Guess the number (1-100): "))
            guesses += 1

            if user_input < number:
                print("📉 Lower guess! Try a higher number.")
            elif user_input > number:
                print("📈 Higher guess! Try a lower number.")
            else:
                print(f"🎉 Correct! You guessed the number in {guesses} attempts.")
                break

        except ValueError:
            print("⚠️ Please enter a valid number!")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()