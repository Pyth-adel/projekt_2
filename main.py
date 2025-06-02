"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Tvé jméno
email: tvůj@email.cz
"""

import random

def generate_number():
    digits = list("123456789")  # první číslo nesmí být 0
    first_digit = random.choice(digits)
    digits = list("0123456789")
    digits.remove(first_digit)
    rest_digits = random.sample([d for d in digits if d != first_digit], 3)
    return first_digit + ''.join(rest_digits)

def welcome_message():
    print("Hi there!")
    print("-" * 60)
    print("I've generated a random 4 digit number for you.")
    print("Let's play a bulls and cows game.")
    print("-" * 60)

def is_valid_guess(guess):
    return (
        guess.isdigit() and
        len(guess) == 4 and
        len(set(guess)) == 4 and
        guess[0] != '0'
    )

def evaluate_guess(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(min(secret.count(d), guess.count(d)) for d in set(guess)) - bulls
    return bulls, cows

def main():
    secret_number = generate_number()
    attempts = 0
    welcome_message()

    while True:
        guess = input("Enter a number: ")
        if not is_valid_guess(guess):
            print("Invalid input. Enter 4 unique digits, number cannot start with 0.")
            continue

        attempts += 1
        bulls, cows = evaluate_guess(secret_number, guess)

        bulls_text = "bull" if bulls == 1 else "bulls"
        cows_text = "cow" if cows == 1 else "cows"
        print(f"{bulls} {bulls_text}, {cows} {cows_text}")

        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts} guesses!")
            print("That's amazing!")
            break

if __name__ == "__main__":
    main()
