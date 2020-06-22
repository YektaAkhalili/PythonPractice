pizza = {
	'crust':'thick',
	'toppings':['mushrooms','cheese'],
}

print("You wanted a " + pizza['crust'] + "-crust pizza with these toppings:")

for topping in pizza['toppings']:
	print("\t " + topping)