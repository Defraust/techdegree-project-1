"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game(score, ongoing_game):
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

    while ongoing_game:
        try:
            one_more_time = input("\nWould you like to play again? 'YES' or 'NO'? > ")
            one_more_time = one_more_time.upper()
            if one_more_time == 'YES' or one_more_time[0] == 'Y':
                if attempts < high_score:
                    start_game(attempts, True)
                    ongoing_game = False
                else:
                    start_game(high_score, True)
                    ongoing_game = False
            elif one_more_time == 'NO' or one_more_time[0] == 'N':
                print("\nThanks for playing! Come back soon!\n")
                ongoing_game = False
            else:
                raise ValueError
        except KeyboardInterrupt:
            print("\n\nBye!\n")
            ongoing_game = False
        except ValueError:
            print("\nSorry, I didn't understand that. Exiting.")
            ongoing_game = True


if __name__ == '__main__':
    start_game(10, True)

'''
 Credit to a user 'Bubbles' on a Programming discord for
 helping with the second while loop. Originally if several
 games were played in a row my own while loop would cause
 it to take several 'NO' responses to exit.
 '''
