# lots of animals
my_list = ['aardvark', 'bat', 'cat', 'dog', 'elephant', 'frog', 'gorilla', 'hippopotamus', 'iguana', 'jellyfish', 'koala', 'lamprey', 'moose', 'newt', 'octopus', 'panda', 'quail', 'rabbit', 'snail', 'tapir', 'unicorn', 'vulture', 'wasp', 'x-ray tetra', 'yak', 'zebra']

# How long is my list?
print(f"my_list is {len(my_list)} items long")

# Appending an item to the list
my_list.append(input("What animal would you like to add? >>> "))

# How long is the list now? Print the value out
print(f"my_list is now {len(my_list)} items long")

# Add three more animals to the list, then print the list
my_list.append('human')
my_list.append('fish')
my_list.append('monkey')
print(my_list)