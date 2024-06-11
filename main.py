#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
mylist4 = []
mylist1 = []
for i in range(0, nr_letters):
    aplha = random.randint(0, len(letters) - 1)
    print(letters[aplha])

    mylist1.append(letters[aplha])
print(mylist1)

mylist2 = []
for i in range(0, nr_symbols):
    aplha = random.randint(0, len(symbols) - 1)
    print(symbols[aplha])
    mylist2.append(symbols[aplha])
print(mylist2)

mylist3 = []
for i in range(0, nr_numbers):
    aplha = random.randint(0, len(numbers) - 1)
    print(numbers[aplha])
    mylist3.append(numbers[aplha])
print(mylist3)

mylist4 = mylist1 + mylist2 + mylist3
random.shuffle(mylist4)
print(mylist4)
string1 = " ".join(mylist4)
print(string1)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
