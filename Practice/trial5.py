# Manchester city has 88 points and Arsenal has 86 points. A win,draw,loss is worth 3,1, and 0 points respectively. 
# Use if-else statemens in python to predict the winner depending on the results and ask the user for the results

ManchesterCity = 88
Arsenal = 86

ManchesterCity_result = input("Enter the latest results of Manchester City(win, draw, loss): ")
Arsenal_result = input("Enter the latest result of Arsenal(win,draw,loss): ")

if ManchesterCity_result == "win":
    ManchesterCity + 3
elif ManchesterCity_result == "draw":
    ManchesterCity + 1
elif ManchesterCity_result == "loss":
    ManchesterCity + 0
else:
    print("Invalid answer")
    print("You choose between win, draw or loss")


if Arsenal_result == "win":
    Arsenal + 3
elif Arsenal_result == "draw":
    Arsenal + 1
elif Arsenal_result == "loss":
    Arsenal + 0
else:
    print("Invalid answer")
    print("You choose between win, draw or loss")


# predict the winner

if Arsenal > ManchesterCity:
    print("Arsenal wins the league")
elif Arsenal < ManchesterCity:
    print("Manchester City wins the league")
elif ManchesterCity == Arsenal:
    print("It's a tie")
else:
    print("You didn't fill in correctly")
