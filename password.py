import string
import random
from tkinter import *


def generate_password():
    # Ask user about the number of characters
    characters_number = int(entry.get())
    # shuffle all lists
    random.shuffle(s1)
    random.shuffle(s2)
    random.shuffle(s3)
    random.shuffle(s4)

    # calculate 30% & 20% of number of characters
    part1 = round(characters_number * (30/100))
    part2 = round(characters_number * (20/100))
    
    # generation of the password (60% letters and 40% digits & punctuations)
    result = []

    for x in range(part1):
        result.append(s1[x])
        result.append(s2[x])

    for x in range(part2):
        result.append(s3[x])
        result.append(s4[x])

    # shuffle result
    random.shuffle(result)

    # join result
    password = "".join(result)
    password_label1.config(text=f"Strong Password: ")
    password_label2.config(text=password)


# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)


# create tkinter window
root = Tk()
root.title("Password Generator")


# create label
label = Label(root, text="How many characters do you want in your password?")
label.pack()


# create entry
entry = Entry(root)
entry.pack()


# create button
button = Button(root, text="Generate Password", command=generate_password)
button.pack()


# create label to display password
password_label1 = Label(root, text="")
password_label2 = Label(root, text="", fg='red')
password_label1.pack()
password_label2.pack()


# run tkinter window
root.mainloop()