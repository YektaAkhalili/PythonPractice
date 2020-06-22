def getName(first_name,last_name):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name

names = []
def putInList(name):
    names.append(name)
    return names

print("Hi. Welcome to the sign up sheet.")


while True:
    flag = input("\npress c to continue, q to quit.")
    if (flag == 'c' or flag == 'C'):
        f_name = input("Your first name: ")
        l_name = input("Your last name: ")
        print("You've successfully signed up as: " + getName(f_name,l_name))
        putInList(getName(f_name,l_name))
        continue
    if (flag == 'q' or flag == 'Q'):    
        print("\nSorry to see you go.")
        break

print("\nPeople who've signed up are: ")        
print(names)



