def Repeat():
    print("Is this annoying yet?")

print("Let's play!")

userInput = "If you want to stop say 'quit'!"
userInput += "\nIf you want to keep going, say nothing!"

answer = ""
while answer != 'quit':
    answer = input(userInput)
    Repeat()

print("Ok, Bye!")    


