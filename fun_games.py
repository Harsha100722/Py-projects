def random_number():
    import random
    ran = random.randint(1, 100)
    while True:
        x = int(input("Guess the number from 1 to 100 💭: "))
        if x < ran:
            print("Guess higher number!👆")
        elif x > ran:
            print("Guess lower number!👇")
        else:
            print("Congratulations! Your guess is correct.🎉")
            break

def rock_paper_scissor():
    import random
    while True:
        choices = ('r', 's', 'p')
        bot = random.choice(choices)
        user = input("Enter your choice (rock🪨/paper📃/scissor✂️ ) as (r/p/s): ")
        if user not in choices:
            print("Enter a valid character!")
            break
        if (bot == 'r' and user == 'p') or (bot == 'p' and user == 's') or (bot == 's' and user == 'r'):
            print(f"You won! USER choosed {user} beats BOT choosed {bot}")
            q = input("Do you want to play again? (y/n): ").lower()
            if q == 'n':
                break
        elif bot == user:
            print(f"Both choose {bot}. It's a tie, try again...")
        else:
            print(f"You lost! BOT choosed {bot} beats USER choosed {user}")

while True:
    try:
        x = int(input("Enter a number (1 for guessing game, 2 for rock-paper-scissor, 0 to quit): "))
        if x == 1:
            random_number()
        elif x == 2:
            rock_paper_scissor()
        elif x == 0:
            print("Exiting the program!")
            break
        else:
            print("Please enter 1, 2, or 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")
