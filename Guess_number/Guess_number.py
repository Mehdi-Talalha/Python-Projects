import random
import colorama
from colorama import Fore, Style

# Initialize colorama
colorama.init(autoreset=True)


def guess_number_game():
    while True:
        number_to_guess = random.randint(0, 100)
        attempts = 0

        print(Fore.CYAN + "\n🎯 Guess The Number Game!")
        print(Fore.CYAN + "Guess a number between 0 and 100")

        while True:
            try:
                guess = int(input("Your guess: "))
            except ValueError:
                print(Fore.YELLOW + "Invalid data type. Please enter an integer.")
                continue

            if guess < 0 or guess > 100:
                print(Fore.YELLOW + "Invalid number. Stay between 0 and 100.")
                continue

            attempts += 1

            if guess < number_to_guess:
                print(Fore.RED + "Too low!")
            elif guess > number_to_guess:
                print(Fore.RED + "Too high!")
            else:
                print(
                    Fore.GREEN
                    + f"🎉 Congratulations! You guessed {number_to_guess} in {attempts} attempts."
                )
                break

        # Replay section
        again = input(Fore.CYAN + "Play again? (y/n): ").lower()

        if again != "y":
            print(Fore.MAGENTA + "Thanks for playing 👋")
            break


if __name__ == "__main__":
    guess_number_game()