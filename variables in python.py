#Diffrent variable present in Python
#Python doesnt require you to declare variable type.

#Strings

taste = "sweet" # you need inverted comma for strings unlike other data types
food = "sugar"

eat = taste + " " + food

print( "I love " + eat)
print(type(eat)) # type() function is used to find data type of a variable.

# Integer

rate = 8
rate += 1

print("I give it rating of: " + str(rate)) # str() is used to convert a variable type. This is know as type casting.
# We cannot print variable of two diffrent data type. Thus we need to use type casting.
print(type(rate))

# Float

weight = 23.5

print("I need: " + str(weight) + " grams of it")
print(type(weight))

#boolean

truth = True
print("Do I love my sugar:"+ str(truth))
print(type(truth))