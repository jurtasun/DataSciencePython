# Data science in Python course
# Jesus Urtasun - January 2021
# Week 1 - exercise 2

print("Data science in Python")
print("Week 1 - exercise 2")

import re

# Regular expression
print("\nRegular expression")

# 1. Basic regex API

# Create some text for example
text = "this is a good day"

# Look for a particular string match
if re.search("good", text):
    print("Match")
else:
    print("No match")

# Try segment a string, the so called "tokenizin", or separating a string based on patterns
text = "Amy works diligently. Amy gets good grades. Amy is succesul"

my_list1 = re.split("Amy", text)
print("my list 1:\n", my_list1)

my_list2 = re.findall("Amy", text)
print("my list 2:\n", my_list2)

# 2. Complex patterns