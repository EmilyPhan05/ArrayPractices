import random

#creates original list
first = [0] * 3

#fills the list, then prints it
for i in range(len(first)):
    first[i] = random.randint(0, 200)

print(first)

#creates a second list to hold the binary representations of the first
binary = first

#fills the new list with binary representations, then prints the list
for i in range(len(first)):
    binary[i] = bin(binary[i])

print(binary)

#creates a third list to hold the adjusted binary values
negative = [""]

#if a value has a 101 in it, it is made negative
#otherwise, 00 is added to the end of the number
for pos in range(len(binary)):
    current = binary[pos]
    if "101" in str(current):
        new = int(current, 2)
        new *= -1
        new2 = bin(new)
        negative.append(new2)
    else:
        current += "00"
        negative.append(current)

negative.remove(negative[0])
print(negative)

#creates the last list to hold the base ten representations of the "negative" list
final = negative

#converts each number to base ten
for i in range(len(final)):
    current = int(final[i], 2)
    final[i] = current

print(final)