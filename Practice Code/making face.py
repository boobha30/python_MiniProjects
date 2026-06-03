user_input = input("Enter a word with an emoticon: ")
new_input = user_input.replace(":)", "😊").replace("(:", "😊").replace(":(", "😞").replace(";)", "😉")
print(new_input)