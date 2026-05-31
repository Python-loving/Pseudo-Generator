from tkinter import *
from main import *

window = Tk()

window.title("You pseudo")
window.geometry("720x480")
window.config(bg="black")
window.iconbitmap("image.ico")

# On crée une frame
frame = Frame(window, bg="black")


# on definie le title
window_title = Label(window, text="Voicis vos pseudo", bg="black", fg="white")
window_title.pack(pady=10)

# Affichage des pseudo
window_pseudo = Label(frame, font=("Arial"), bg="black", fg="white")
window_pseudo.pack()

def gen():
    result = ai()
    window_pseudo.config(text=result)


# on fais notre button
window_button = Button(frame, text="Click Pour generer 10 pseudo", font=("Arial"), bg="blue", fg="white", activebackground="blue", command=gen)
window_button.pack()

frame.pack(expand=True)

window.mainloop()