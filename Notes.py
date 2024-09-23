'''
    Lesson: Typecasting
    Author: Mr. Kalisz
    Date Creatd: Sept 23, 2024
    Date Last Modified: Sept 23, 2024
'''

#Typecasting - converting data types

#Type out the function for the data type you want to convert to, put the value inside the brackets

#Create a copy of the value in the given data type
#str()
#int()
#float()

num = 3

#In order to replace num with a float version, we need to assign to it
num = float(num)

print(str(num) + " hello")

#Rules
#Typecasting can be done all the time when going from a less complicated to a more complicated type

#int -> float

#without typecasting
num = 2
print(num + 0.0) 

print(float(num))

#int -> str
#float -> str
#boolean -> str

#The otherway around only works sometimes

word = "57.5" 

#if the data can not be stored in the new data type, it will crash
#print(int(word)) #when a value is valid, the typecasting works

#float -> int 
#removes the decimal point and everything after it

num = 3.5
print(int(num))