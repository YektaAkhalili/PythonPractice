active = True
movies = {} 
while active:
    name = input("What's your name? ")
    response = input("What's your favorite movie? ")

    movies[name] = response

    repeat = input("would you like someone else to answer? y/n")
    if repeat == 'n':
        active = False

print("\n---polling results---")

for name, movie in movies.items():
    print(name.title() + "'s favorite film is: " + movie.title())
