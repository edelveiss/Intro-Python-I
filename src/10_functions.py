# Write a function is_even that will return true if the passed-in number is even.

def is_even(number):
    return number % 2 == 0


def get_user_choice(w_string):
    choice = input(w_string)
    return choice

# Print out "Even!" if the number is even. Otherwise print "Odd"
def even_or_odd(number):
    if is_even(number):
        print("Even!" )
    else:
        print("Odd")

welcome_string = "Enter a number or q to quit: "
### First user choice
user_choice = get_user_choice(welcome_string)


while user_choice.lower() != "q":
    if user_choice.isnumeric():
        even_or_odd(int(user_choice))
        user_choice = get_user_choice(welcome_string)
    else:
        user_choice = get_user_choice(f"{user_choice} is not a number.{welcome_string}")

    

