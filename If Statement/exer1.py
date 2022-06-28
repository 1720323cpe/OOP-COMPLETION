#Color Ball Game 1
ball_color = "green", "yellow", "red"
ball_color = input('enter ball color:')
if (ball_color) == "green":
    print("you just earned five points.")
else:
    print("no points.")
    

# Color Ball Game 1 Fail
ball_color = "green", "yellow", "red"
ball_color = input('enter ball color:')
if (ball_color) != "green":
    print("you just earned five points.")
else:
    print("no points.")