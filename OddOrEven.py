def decisionNumber(a):
    if a % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")

#we're gonna ask the user for a number 
number = int(input("Enter a number: "))
decisionNumber(number)
