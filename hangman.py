
from tkinter import *
from tkinter import messagebox
import random

window = Tk()
window.title("Hangman")

word_list = ["guava","lyche","grape","peach","mango","melon","apple"]

photos = [PhotoImage(file="images/hang0.png"), PhotoImage(file="images/hang1.png"), PhotoImage(file="images/hang2.png"), PhotoImage(file="images/hang3.png"), PhotoImage(file="images/hang4.png"), PhotoImage(file="images/hang5.png"), PhotoImage(file="images/hang6.png"), PhotoImage(file="images/hang7.png"), PhotoImage(file="images/hang8.png"), PhotoImage(file="images/hang9.png"), PhotoImage(file="images/hang10.png"), PhotoImage(file="images/hang11.png")]

the_word_withSpaces = ""
numberOfGuesses = 0
the_word = ""

def newGame():
    global the_word_withSpaces
    global numberOfGuesses
    global the_word
    numberOfGuesses = 0

    the_word = random.choice(word_list)
    the_word_withSpaces = " ".join(the_word)
    lblWord.set(' '.join("_" * len(the_word)))

def guess(letter):
    global numberOfGuesses
    global the_word
    
    if numberOfGuesses < 11:
        if letter.isalpha():
            txt = list(the_word_withSpaces)
            guessed = list(lblWord.get())
            if the_word_withSpaces.count(letter) > 0:
                for c in range(len(txt)):
                    if txt[c] == letter:
                        guessed[c] = letter
                lblWord.set("".join(guessed))
                if lblWord.get() == the_word_withSpaces:
                    messagebox.showinfo("Hangman", "You Guessed It!")
            else:
                numberOfGuesses += 1
                imgLabel.config(image=photos[numberOfGuesses])
                if numberOfGuesses == 11:
                    message_ = "You Lost!\nThe Word Is :" + the_word
                    messagebox.showwarning("Hangman", message_)

def on_key(event):
    guess(event.char.lower())

hangman_label = Label(window, text="Hangman", font=('Arial', 24, 'bold'))
hangman_label.place(x=200, y=10)

imgLabel = Label(window)
imgLabel.place(x=25, y=53)

lblWord = StringVar()
Label(window, textvariable=lblWord, font=('consolas 24 bold')).place(x=190, y=145)
window.bind('<KeyPress>', on_key)

window.geometry("545x250")
window.resizable(width=False, height=False)
newGame()

window.mainloop()
