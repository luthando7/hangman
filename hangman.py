# Hangman game


def capture_user_input():
    """
    blah
    """
    guess = ""
    while True:
        try:
            guess = input("Enter 4 digits seperated by commas: ")
            if guess == "exit":
                break
            user_in = guess.split(',')

            for number in user_in:
                if not number.isdigit() or len(user_in) != 4:
                    print("Please enter only digits")
                    raise IOError()
            return user_in
        except IOError:
            continue


def main():
    """
    Main driver function
    """

    code_to_guess = [1, 2, 3, 4]

    tries = 12
    while True:
        correct_numbers = 0
        correct_places = 0
        if tries > 0:
            print(f"You have {tries} tries left")
            tries = tries - 1
            user_guess = capture_user_input()
            print(user_guess)
            for idx, val in enumerate(user_guess):
                if int(val) in code_to_guess:
                    correct_numbers += 1
                    if code_to_guess[idx] == int(val):
                        correct_places += 1
            print(f"You have {correct_numbers} correct number")
            print(f"You have {correct_places} numbers in the right place.")
            if correct_places == 4:
                print("You have won!!!")
                break


if __name__ == '__main__':
    main()
