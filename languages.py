database = {
	'jen': ['python','ruby'],
	'sarah':['c'],
	'edward':['ruby', 'c'],
	'phil':['python','haskell'],
}

for name, lang in database.items():
	if len(lang) > 1:
		print(name.title() + "'s favorite languages are: ")
		for lan in lang:
			print("\t" + lan.title())
	else:
		print(name.title() + "'s favorite language is:" + "\n\t" + lan.title())
	

		