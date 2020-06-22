
def GiveMeAName():
    prompt = "This is the first time you're here."
    prompt += "\nWhat's your name?"
    name = input(prompt) 
    return name

print("Nice to meet you, " + GiveMeAName())

