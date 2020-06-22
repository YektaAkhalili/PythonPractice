users = {
	'aeinstein': {
		'first':'albert',
		'last':'einstein',
		'location':'princeton',
	},

	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
	},
}

for key, value in users.items():
	print("\nUsername: " + key)
	print("\tFull name: " + value['first'].title() + " " + value['last'].title())
	print("\tLocation: " + value['location'].title())