VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    """Ask for color, lowercase it, check if 'quit' is entered, if so print
       'bye' and break, next check if given color is in VALID_COLORS, if not,
       continue, finally if that check passes, print the color"""
    while True:
        in_colour = input("enter a colour")
        in_colour.lower()
        if in_colour == "quit":
            print("bye")
            break
        else:
            for i in VALID_COLORS:
                if in_colour == i:
                    print(i)
                else:
                    continue
