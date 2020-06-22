def repeat():
    print("Is this annoying?")


flag = True
while flag: 
    message = input("yes or no?\n")

    if message == 'yes':
        repeat()
    elif message == 'no':
        flag = False
        print("ok, bye!")
