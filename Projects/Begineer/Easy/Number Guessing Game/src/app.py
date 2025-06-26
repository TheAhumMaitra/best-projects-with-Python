#Number Guessing Game in Python
import random

def main() :
    try:
        ask_range = int(input("Enter the upper limit of the random number range.\n Starting number is always 0. You should enter the last number in range.\n Example: 255 (Means range 0 to 255)\n>"))
        rand_number = random.randint(0,ask_range)
        print(f'You chose the random number range from 0 to {ask_range}.')
        ask_guess = int(input("Enter you guess : \n Example : 21\n>"))
        while True :
            if ask_guess < rand_number :
                print(f"You gussed - {ask_guess}. Thats too low..")
                ask_guess = int(input("Enter you guess : \n Eg : 21\n>"))
            elif ask_guess > rand_number :
                print(f"You gussed {ask_guess} and that's too high....")
                ask_guess = int(input("Enter you guess : \n Eg : 21\n>"))

            if ask_guess == rand_number :
                print(f"You gussed {ask_guess} and that's correct!")
                break
    except ValueError :
        print(f"That's not a valid number! Please enter a valid integer....You guessed - {ask_guess}")
main()
