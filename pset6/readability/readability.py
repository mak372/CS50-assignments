from cs50 import get_string
import math
num_letters = 0
num_words = 0
num_sentences = 0
l= 0.00
s = 0.00
index = 0
x = get_string("Text:")
a = len(x)
for i in range(a):
    if x[i].isalpha():
        num_letters += 1
    if (x[i].isalpha() and x[i+1] == ' ') or (x[i].isalpha() and x[i+1] == ',') or (x[i].isalpha() and x[i+1] == '.') or(x[i].isalpha() and x[i+1] == '!') or(x[i].isalpha() and x[i+1] == ':') or (x[i].isalpha() and x[i+1] == ';') or (x[i].isalpha() and x[i+1] == '?'):
        num_words += 1
    if x[i] == '.' or x[i] == '!' or x[i] == '?':
        num_sentences += 1

print(f"letters {num_letters}\n",end="")
print(f"words {num_words}\n",end="")
print(f"sentences {num_sentences}\n",end="")
l = (num_letters / num_words) * 100
s = (num_sentences / num_words) * 100
index = round(0.0588 * l - 0.296 * s - 15.8)
if index < 1:
    print("Before grade 1\n",end="")
if index > 16:
    print("Grade: 16 +\n",end="")
elif (index > 1 and index < 16):
    print(f"Grade:{index}\n",end="")
