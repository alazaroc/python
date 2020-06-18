# Guessing game
secret_number = 9
guess_limit = 3
guess_count = 0
while guess_count < guess_limit:
    guess = int(input("Guess 1 to 10: "))
    guess_count += 1
    if guess == secret_number:
        print("You win!")
        break
else:
    print("Try again")
