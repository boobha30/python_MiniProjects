username="thiaguboobhashri@gmail.com"
password="Boobhashri12340987"
attempts = 2
login=False
user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")
while login==False and attempts > 0:
    def login_system():
        if user_name!=username:
            print("Invalid username. Please try again.")
        elif pass_word!=password:
            print("Invalid password. Please try again.")
        else:
            print("Login successful!")
            login=True
    login_system()
    for i in range(attempts):
        if login==False:
            attempts -= 1
            user_name = input("Enter your username: ")
            pass_word = input("Enter your password: ")
            login_system()
        else:
            login=True
    if attempts == 0:
        print("Too many failed attempts. Please try again later.")