def getName(first_name,last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

print("Tell me your full name please.")

while True:
    print("If you want to quit, press q")

    f_name = input("Your first name:")
    if f_name == 'q':
        print("we're sad to see you go!")
        break

    l_name = input("Your last name:")
    if l_name == 'q':
        print("we're sad to see you go!")
        break 

    print("Hello there, " + getName(f_name,l_name))

    
    