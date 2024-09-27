
def example_a():
    print('\nExample A')
    print('~~~~~~~~~')

    user_input = 0
    apples = 10
    i = 2.5
    is_active = True

    if is_active:
        # You can't divide by 0.
        # It will run but will fail, a "run time" error.
        ans = 10 / user_input
        print(f"10 / {user_input} is {ans}")

        # TESTING - Andy 29/Oct/24
        print(f"Test: apples is of type {type(apples)}")
        print(f"Test: i is of type {type(i)}")

        # In C# you CAN'T divide a double (floating point number) by an integer.
        # You would get a compile time error, the program would not build.
        # In Python, you CAN divide an integer by a float - the answer will just be in float format!
        ans2 = apples / i
        print(f"{apples} / {i} is {ans2}")


def example_b():
    print('\nExample B')
    print('~~~~~~~~~')

    try:
        user_input = 0

        i = 0
        while i < 5:
            ans = 10 / user_input
            print(f"10 / {user_input} is {ans}")

            if i == 3:
                # This creates a new exception.
                # Read up on "throwing exceptions"
                raise Exception("Test Exception")

            i += 1
    except ZeroDivisionError as e:
        # This will catch the ZeroDivisionError error ONLY
        print(f"Sorry, you can't divide by zero! Error: {e}")
    except Exception as e:
        # This will catch every other error
        print(f"General Error: {e}")


# Puzzle A - Get Past Gandalf
# Add a try-except block to this code and debug it.
def puzzle_a():
    print('\nPuzzle A')
    print('~~~~~~~~~')

    challenge = None

    print("Gandalf: 'You shall not pass!'...")
    user_input = input("Try and pass? y/n:")

    if user_input.lower() == "y":
        uppercase_input = challenge.upper()
        print(f"{uppercase_input}")
    else:
        print("Gandalf: 'Phew, I thought you were going to try and pass! Slow down!'...")


# Puzzle B - Format me not
# Add a try-except block to this code and debug it.
def puzzle_b():
    print('\nPuzzle B')
    print('~~~~~~~~~')

    user_input = 0.0

    user_input = int(input("Enter a number with a floating point:"))

    print("Your number was {1}".format(user_input))


# Puzzle C - Not my type
# Add a try-except block to this code and debug it.
def puzzle_c():
    print('\nPuzzle C')
    print('~~~~~~~~~')

    bank = 100

    user_input = input("How much money would you link to add to your bank account?:")

    bank = bank + user_input

    print(f"Your new bank balance is {bank}")


if __name__ == '__main__':
    # Run the puzzles

    example_a()
    example_b()

    # puzzle_a()
    # puzzle_b()
    # puzzle_c()
