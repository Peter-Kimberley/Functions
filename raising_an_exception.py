# An example of an exception raise to force the program to fail.

def banner_text(text=" ", screen_width=80):
    """
    """
    
    
    if len(text) > screen_width - 4:
        raise ValueError("string {0} is larger than specified width {1}"
                         .format(text, screen_width))
   

    if text == '*':
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("*",40)
banner_text("Hello World",40)
banner_text("*",40)
banner_text(screen_width=40)
banner_text("*",40)
banner_text("Hello World",40)
banner_text("*",40)