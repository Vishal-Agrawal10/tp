import sys

test_taker_name = "Blat"
n_number = "N00829601"
print("Enter the word : ", end ='', file = sys.stderr)
word = input()

if word > test_taker_name:
    print("After")
elif word < test_taker_name:
    print("Before")
elif word == test_taker_name:
    print("That is my name")
