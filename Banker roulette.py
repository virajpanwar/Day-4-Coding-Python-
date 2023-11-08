#Bankers Roulette
import random

names_str=input("Enter everybody's name separated by commas and a space: ")
names=names_str.split(", ")
nl=len(names)
rp=random.randint(0,nl-1)
print("The person paying the bill is "+names[rp])
