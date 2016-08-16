#!/usr/bin/env python
#
# Mims Place-in Exam 1
# Mastermind
#
# usage: python mimsmind1.py [length]
##############################################################################

from random import randint
import sys

def guess_a_number():
    """Asks the user to guess a random number"""
    
    # Checks to see if the program is run with extra arguments
    # else provides a default argument
    if len(sys.argv) > 1:
        num_digits = int(sys.argv[1])
    else:
        num_digits = 3
    secret_number = 3#randint(0, 10**num_digits - 1)
    secret_number = to_0_padded_string(secret_number, num_digits)
    guesses = 0
    maxrounds = (2**num_digits) + num_digits
    guessed_correctly = False
    prompt = ("Please guess a {}-digit number. You have {} tries. "
            .format(num_digits, maxrounds))
    for n in range(maxrounds):
        user_input = input(prompt)
        # Validate user input
        try:
            int(user_input)
        except ValueError:
            print("Invalid input. Please type non-word numerals.")
        else:
            if len(user_input) > num_digits:
                print("Invalid input. You have entered too many digits.")
                
            # Pad the left hand side with enough 0's to make it n digits.
            elif len(user_input) < num_digits:
                user_input = to_0_padded_string(user_input, num_digits)
                print(("The zero padded equivalent is {}. This is compared with the secret number to determine bulls and cows."
                    .format(user_input)))
            guesses += 1
            # Reinitialize the bulls and cows for each guess
            bulls = 0
            cows = 0
            if user_input == secret_number:
                guessed_correctly = True
                print(("Congratulations! You guessed the correct number in {} {}!"
                    .format(guesses, "try" if guesses==1 else "tries")))
                break
            cow_chars = []
            lst_secret_num = list(secret_number)
            # Iterate simultaneously through user_input and secret_number
            for char, digit in list(zip(user_input, secret_number)):
                if char == digit:
                    bulls += 1
                else:
                    # Second boolean expression checks the edge case:
                    # user_input = 111, secret_number = 123
                    # then bulls: 1, cows: 1, i.e. it will not double
                    # count the cows
                    if char in lst_secret_num and char not in cow_chars:
                        cows += 1
                        cow_chars.append(char)
                    
            # Don't say 'Try again' if the user is out of guesses        
            prompt = ("bull(s): {}, cow(s): {}. {}"
                .format(bulls, cows, "" if guesses==maxrounds else "Try again. "))

    if not guessed_correctly:
        print("Sorry, you are out of tries. The correct number was {}.".format(secret_number))
     
def to_0_padded_string(number, num_digits):
    """Changes a number to a 0-padded string
    E.g. 2 will change to 002 if the number of digits is 3
    
    Parameters:
    number -- the number to pad with 0's
    num_digits -- the number of digits that the final padded number will have
    """
    if int(number) < (10**(num_digits - 1)):
        number = str(number)
        number = "0"*(num_digits - len(number)) + number
        return number
    return str(number)
    
def main():
    guess_a_number()

if __name__ == "__main__":
    main()