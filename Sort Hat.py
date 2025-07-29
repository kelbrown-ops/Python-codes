# Write code below 💖
Gryffindor = 0
Hufflepuff = 0
Ravenclaw = 0
Slytherin = 0

print("=======")
print("Sorting Hat Game ")
print("=======")

print(" Q1) Do you like Dawn ot Dusk? ")
print("1) Dawn")
print("2) Dusk")
answer = int(input("Enter your number (1-2): "))
if answer == 1:
  Gryffindor = Gryffindor + 1
  Ravenclaw = Ravenclaw + 1
elif answer == 2:
  Hufflepuff = Hufflepuff + 1
  Slytherin = Slytherin + 1
else:
  print("Wrong input!")

print(" Q2) When Im dead, I want people to remember me as: ")
print("""
1) The Good
2) The Great
3) The Wise
4) The Bold""")
answer = int(input("Enter your number (1-4): "))
if answer == 1:
  Hufflepuff = Hufflepuff + 2
elif answer == 2:
  Slytherin = Slytherin + 2
elif answer == 3:
  Ravenclaw = Ravenclaw + 2
elif answer == 4:
  Gryffindor = Gryffindor + 2
else:
  print("Wrong input!")

print(" Q3) Which kind of instrument most pleases your ear?")
print("""1) The violin
    2) The trumpet
    3) The piano
    4) The drum
""")
answer = int(input("Enter your number (1-4): "))
if answer == 1:
  Hufflepuff = Hufflepuff + 4
elif answer == 2:
  Slytherin = Slytherin + 4
elif answer == 3:
  Ravenclaw = Ravenclaw + 4
elif answer == 4:
  Gryffindor = Gryffindor + 4
else:
  print("Wrong input!")
print("         ")
print("The final results are as follows: ")
print(f" 🦁 Gryffindor:  {Gryffindor} ")
print(f" 🦅 Ravenclaw:   {Ravenclaw} ")
print(f" 🦡 Hufflepuff:  {Hufflepuff} ")
print(f" 🐍 Slytherin:   {Slytherin} ")