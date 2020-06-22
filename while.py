uncoonfirmed_users = ['alice','brian','candace']
confirmed_users = []

while uncoonfirmed_users:
    current_user = uncoonfirmed_users.pop()
    print("Verifying user: "+ current_user.title())
    confirmed_users.append(current_user)

print("\nThe following usres have been confirmed: ")
for user in confirmed_users:
    print(user.title())