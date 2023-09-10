from myAPI import *

from tkinter import *

from PIL import *

from tkinter import ttk

root = Tk()


options = [
    "Biography", "Music", "Romance","Family", "War", "News", "Reality",
    "Talk Show", "Adventure","Fantasy", "Animation", "Drama", "Film Noir",
    "Horror", "Action","Game Show", "Comedy", "History", "Western",
    "Musical", "Sport","Thriller", "Short", "Adult", "Crime", "Science Fiction", "Mystery",
    "Documentary"
]

def show():
    movie = getRandomMovie(getMoviesFromFile(moviesToID[clicked.get()]))
    myLabel = Label(root, text=movie).pack()

def showUpdate():
    updateTextFile(moviesToID[clicked.get()])
    myLabel = Label(root, text="UPDATED!!").pack()


# def show():
#     myLabel = Label(root, text = "Trial")
#     myLabel.pack()

clicked = StringVar(root)
clicked.set("Choose a Genre")

drop = OptionMenu(root, clicked, *options)
drop.pack()
myButton = Button(root, text = "SHOW MOVIE!", bg = "green", command = show )
myButton.pack()
#myButton.config(height = 40, width = 40)
myButton2 = Button(root, text = "UPDATE GENRE", command = showUpdate )
myButton2.pack()
#myButton2.config(height = 40, width = 40)

root.mainloop()



