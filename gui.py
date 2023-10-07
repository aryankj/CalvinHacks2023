import tkinter as tk
from tkinter import StringVar, OptionMenu, Label, Button
from myAPI import get_random_movie, get_movies_from_file, update_text_file, moviesToID

class MovieApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Genre Selector")

        self.options = [
            "Biography", "Music", "Romance", "Family", "War", "News", "Reality",
            "Talk Show", "Adventure", "Fantasy", "Animation", "Drama", "Film Noir",
            "Horror", "Action", "Game Show", "Comedy", "History", "Western",
            "Musical", "Sport", "Thriller", "Short", "Adult", "Crime",
            "Science Fiction", "Mystery", "Documentary"
        ]

        # Create a custom style for buttons
        self.button_style = {
            'bg': 'green',
            'fg': 'white',
            'font': ('Helvetica', 12),
        }

        self.layout = tk.Frame(root)
        self.layout.pack(padx=10, pady=10)

        self.spinner = OptionMenu(
            self.layout,
            StringVar(),
            *self.options
        )
        self.spinner.config(width=20)
        self.spinner.grid(row=0, column=0, padx=10, pady=10)

        self.show_button = Button(
            self.layout,
            text='SHOW MOVIE!',
            command=self.show_movie,
            **self.button_style
        )
        self.show_button.grid(row=1, column=0, padx=10, pady=10)

        self.update_button = Button(
            self.layout,
            text='UPDATE GENRE',
            command=self.update_genre,
            **self.button_style
        )
        self.update_button.grid(row=1, column=1, padx=10, pady=10)

        self.result_label = Label(
            self.layout,
            text='',
            wraplength=400
        )
        self.result_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    def show_movie(self):
        selected_genre = self.spinner.cget("text")
        if selected_genre != 'Choose a Genre':
            movie = get_random_movie(get_movies_from_file(moviesToID[selected_genre]))
            self.result_label.config(text=movie)
        else:
            self.result_label.config(text='Please select a genre.')

    def update_genre(self):
        selected_genre = self.spinner.cget("text")
        if selected_genre != 'Choose a Genre':
            update_text_file(moviesToID[selected_genre])
            self.result_label.config(text='UPDATED!!')
        else:
            self.result_label.config(text='Please select a genre.')

if __name__ == '__main__':
    root = tk.Tk()
    app = MovieApp(root)
    root.mainloop()
