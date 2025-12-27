#Basic Python

#Printing Hello World.
print("Hello World!")

#Variable Print
intVar = 7
print(intVar)

#Print Character with Variable
print("This is number Seven:",intVar)

#Input Variable in Python
varInp = input()
print(type(varInp), varInp)  #By default input variable is string type only.

# We need to typecast if need to convert into another datatype

#int input

intInp = int(input())

#input with input text

intInp = int(input("Enter the integer values: "))

#multiple input value at same time

a,b = map(int, input("Enter a and b:").split()) 

#input list 

myList = list(input("Enter list items comma seperated.").split(","))

print(type(myList),myList)
