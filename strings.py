# Create a variable called name and set it equal to your name
name = "Andrew"

# Create a variable called age and set it to your age in years 
# Note: This must be an int, not a string!
age = 40

# Create a variable called place and set it equal to where you live
place = "Ottawa"

# Create a variable called output, and use {} symbols and the format() function to 
# make it contain a string like the example text in the description
string = "hello my name is {} and i am {} years old.  i live in {} and i love python"
output = string.format(name, age, place)
print(output)
