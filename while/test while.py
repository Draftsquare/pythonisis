button_pressed = False

while not button_pressed:
    user_input = input("Press a button or type exit to exit")
    if user_input == "exit":
        break

    if user_input == "desired_button":
        button_pressed = True
        print("nice")
    else:
        print("no press, try")

print("loop ended")
