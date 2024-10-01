greeting = 'Hello'
name = 'Michael'
message = greeting + name
print(message)

message = greeting + ', ' + name
print(message)

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)

print(dir(name))
#print(help(str))
print(help(str.upper))