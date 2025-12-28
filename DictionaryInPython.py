# declaration of dictionary
myVar = {}
#printing type
print(type(myVar))

#adding new elements

myVar["color"] = "black"
print(myVar)

#Updating new value to existing key
myVar["color"] = "red"
print(myVar)


#removing element from dictionary
myVar.pop("color")
print(myVar)

myVar["color1"] = "red"
myVar["color2"] = "black"
print(myVar)

