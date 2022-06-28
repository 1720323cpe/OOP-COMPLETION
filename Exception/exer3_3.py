try:
     ball_color = "green", "yellow", "red"
     ball_color = input('enter ball color:')
     if (ball_color) == "green":
         print("you just earned five points.")
     elif (ball_color) == "yellow":
          print("you just earned 10 points.")
     elif (ball_color) == "red":
          print ("You just earned 15 points.")
     else:
         print("Please input the said color only! :)")

except:
    ('error')