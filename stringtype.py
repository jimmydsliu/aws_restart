myString = "This is a string."
firststring = "water"
secondstring = "fall"
thirdstring = firststring + secondstring


print(myString)
print(type(myString))
print(myString + " is a data type " + (str(type(myString))))

print(thirdstring)

name = input("what is your name?")
print(name)

color = input("what is your favorite color?")
animal = input("what is your favorite animal?")

print("Hi {}, you like a {} {}! ".format(name,color,animal))