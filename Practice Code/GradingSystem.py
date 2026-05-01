mark=input("Enter your mark: ")
if float(mark) >= 90 and float(mark) <= 100:
    print("You have scored an A grade.")
elif float(mark) >= 75 and float(mark) < 90:
    print("You have scored a B grade.")
elif float(mark) >= 50 and float(mark) < 75:
    print("You have scored a C grade.")
elif float(mark) >= 0 and float(mark) < 50:
    print("You have failed.")
else:
    print("Invalid mark.please enter a mark between 0 and 100.")