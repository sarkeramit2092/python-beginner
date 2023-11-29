#strings

print ("Hellow World")

name = "Tim"

print (name)
print (name[2])
print (name.upper())
print (name.lower())
print (name.islower())
print(name.lower().islower())
print (len(name))
print (name.replace("M", "T"))

#numbers

print (100)
number = 99

print (number)
print (10+10)
print (22+7.984)
print (80/2)
print (78*22.86)
print (10%6)
print(abs(-5))
print (max(4, 2, 10))
print (min(2,5,1))
print (round(4.5))
print (bin (3))

#math function

from math import *

print (sqrt(1000))

#user input

name1 = input ("Input Your Name: ")
age = int (input ("Input Your Age: "))

print ("Your name is " + name1 +" and your are", age)

#Word Replacement Exercise

sentence = input ("Enter Your Sentence: ")
print ("Your sentence is: ",sentence)
word1 = input ("Enter the word you want to replace: ")
world2 = input ("Enter the world to replace it with: ")
print (sentence.replace(word1,world2))