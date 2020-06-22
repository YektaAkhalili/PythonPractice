def printName(first_name, last_name, middle_name = ''):
    """Middle name here is an optional value"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name 
    return full_name

name = printName('Yekta','Khalili')
print(name)

full = printName('Yekta','Khalili','Sadat')
print("Full name: \n" + full)