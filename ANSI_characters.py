# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, effect: str) ->None:
    """_summary_

    Args:
        prints 'text' using the ANSI sequences,
        text (str): _description_
        this is the string that will be effected
        effect (str): _description_
        this is the effect that will be applied to the string, 
        this will be one of the constants that were defined,
        at the start of this code.
    """
    output_string = "{0}{1}{2}".format(effect, text, RESET)
    print(output_string)


colour_print("Hello, Red", RED)
# test that the colour was reset
print("This should be in the default terminal colour")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello, Bold", BOLD)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Black", BLACK)


# this is just a piece of test code i have added




    


# print(RED, "This will be red")
# print(BLUE, "This will be Blue")
# print(BOLD, BLACK, UNDERLINE, "This will be black, and bold")
# print("And so is this")