import sys

print("Enter Name : ", end ='', file = sys.stderr)
name = input()
print("Enter Sound : ",end ='', file = sys.stderr)
sound = input()

if name == "cardinal":
  print("red")
elif sound == "loud" and name == "robin":
  print('blue')
elif sound == 'soft':
  print('cyan')
else:
  print('black')
