# Weekley Challange

# Output Names
names = ['John', ' ', 'Amanda', 5]

print(type(names[0]))
for name in names:
    if type(name) == str:
        if name.strip() != '':
            print(name)