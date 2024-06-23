def banner_text(text):
    screen_width = 80
    if len(text) > screen_width - 4:
        print("EEK!")
        print("THE TEXT IS TOO LONFG TO FIT IN THE SPECIFIED WIDTH")

    if text == '*':
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)





banner_text("*")
banner_text("Hello World")
banner_text("*")
