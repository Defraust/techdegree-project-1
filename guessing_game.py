"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game(score):
    solution = random.randint(1, 10)
    high_score = score
    attempts = 0
    welcome_message = "\nWelcome to the Number Guessing Game!"

    print(welcome_message)
    print("The current High Score is {}!\nDo you think you can beat that?".format(high_score))
    print("=" * len(welcome_message))

    while True:
        try:
            guess = int(input("Guess a number between 1 and 10. > "))
            if guess >= 1 and guess <= 10:
                # Only counting valid attempts
                attempts += 1
                if guess > solution:
                    print("\nGuess lower.\n")
                    continue
                elif guess < solution:
                    print("\nGuess higher.\n")
                    continue
                else:
                    print("\nYou got it! It took you {} attempt(s).".format(attempts))
                    break
            else:
                raise ValueError
        except ValueError:
            print("\nWhoops! That's not a number between 1 and 10. \nPlease try again.\n")
        except KeyboardInterrupt:
            print()
            break

    try:
        one_more_time = input("\nWould you like to play again? 'YES' or 'NO'? > ")
        one_more_time = one_more_time.upper()
        if one_more_time == 'YES' or one_more_time[0] == 'Y':
            if attempts < high_score:
                start_game(attempts)
            else:
                start_game(high_score)
        elif one_more_time == 'NO' or one_more_time[0] == 'N':
            print("\nThanks for playing! Come back soon!\n")
        else:
            raise ValueError
    except KeyboardInterrupt:
        print("\n\nBye!\n")
    except ValueError:
        print("\nSorry, I didn't understand that. Exiting.")


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    # Passing a default high score of 10
    start_game(10)
