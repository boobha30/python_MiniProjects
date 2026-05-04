import random
number_to_guess = random.randint(1, 100)
print("Welcome to the Guess the Number Game!")
print("I have selected a number between 1 and 100. Can you guess it?")
while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess < number_to_guess and user_guess >= 1:
        print("Too low! Try a higher number.")
    elif user_guess > number_to_guess and user_guess <= 100:
        print("Too high! Try a lower number.")
    elif user_guess == number_to_guess:
        print("Congratulations! You guessed the number correctly.")
        break
    else:
        print("Invalid input. Please enter a number between 1 and 100.")
    

    