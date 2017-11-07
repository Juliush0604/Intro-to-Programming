# lots of animals
my_list = ['aardvark', 'bat', 'cat', 'dog', 'elephant', 'frog', 'gorilla', 'hippopotamus', 'iguana', 'jellyfish', 'koala', 'lamprey', 'moose', 'newt', 'octopus', 'panda', 'quail', 'rabbit', 'snail', 'tapir', 'unicorn', 'vulture', 'wasp', 'x-ray tetra', 'yak', 'zebra']

# creating a smaller list using a slice of my_list
mini_list = my_list[1:4]

# What will be printed? Include it in a comment right below this
#'bat', 'cat', 'dog'
print(mini_list)

# printing a smaller list containing the first five items
print(my_list[:5])

# Modify the line of code below so that it prints out a list
# consisting of the section from cat through iguana,
# including both of those terms
print(my_list[2:9])

# Do the same for rabbit through viper
#Do you mean vulture?
print(my_list[17:22])

# What happens if you use a slice that is blank for start and end?
# Try it out below
print(my_list[:])

# How about if you use the same index for both start and end?
# Try it out below
print(my_list[5:5])