import sys

programmer_name = "Eliot"
print("Enter your Name : ", end ='', file = sys.stderr)
name = input()

if name == programmer_name:
  print("That is my name!")
else:
  print("{} is different than {}".format(name, programmer_name))
