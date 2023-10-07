# CalvinHacks2023 Movie App Project Documentation

## Introduction

The Movie App is a simple graphical user interface (GUI) application built using the Tkinter library in Python. It allows users to select a movie genre, retrieve a random movie from that genre, and update the list of movies for a selected genre. The app provides a user-friendly interface for movie enthusiasts to discover and manage movie lists.

## Features

The Movie App offers the following features:

1. **Genre Selection**: Users can choose a movie genre from a dropdown list of predefined genres.

2. **Show Movie**: Clicking the "SHOW MOVIE!" button retrieves a random movie from the selected genre and displays it on the interface.

3. **Update Genre**: Clicking the "UPDATE GENRE" button updates the list of movies for the selected genre. This is useful for keeping the movie list up to date.

4. **Result Display**: The app displays the selected movie or a status message in a label below the buttons.

5. **Responsive Buttons**: The size of the buttons adjusts proportionally with the screen size for better user experience.

## Usage

To use the Movie App, follow these steps:

1. **Launch the Application**:
   - Run the Python script containing the Movie App code.
   - A graphical window with the Movie App interface will appear.

2. **Select a Genre**:
   - From the dropdown menu labeled "Choose a Genre," select a movie genre you're interested in.

3. **Show a Movie**:
   - Click the "SHOW MOVIE!" button to retrieve and display a random movie from the selected genre.

4. **Update Genre**:
   - Click the "UPDATE GENRE" button to update the list of movies for the selected genre. This ensures the movie list is current.

5. **View Movie Details**:
   - The selected movie will be displayed in the result label below the buttons. Movie details may include the title, description, and other information.

6. **Repeat as Desired**:
   - You can repeat steps 2 to 5 as many times as you like, exploring different genres and movies.

7. **Exit the Application**:
   - Close the Movie App window when you're finished using it.

## Customization

The Movie App code can be customized and extended as needed:

- **Styling**: You can further customize the appearance of the buttons, labels, and other GUI elements by modifying the styles and layout settings in the code.

- **Additional Genres**: To add more genres to the dropdown menu, simply update the `options` list in the code with the desired genre names.

- **Integration with External Data**: The Movie App is designed to work with external data sources for movie information. Ensure that the `myAPI` module contains the necessary functions for retrieving and updating movie data from your chosen data source.

## Dependencies

The Movie App relies on the following libraries and components:

- Tkinter: The built-in Python library for creating GUI applications.

- `myAPI` (Custom Module): Contains functions for retrieving and managing movie data. Ensure this module is correctly implemented and accessible.

## Authors

- Aryan Jha ([aryankj](https://github.com/aryankj)): Coded `myAPI` and contributed to the UI.
- Alina Sainju ([alinasainju](https://github.com/alinasainju)) : Developed `gui.py`, the tkinter UI. 
While building this app, both of us were first-year computer science students participating in our first Hackathon!

## Conclusion

The Movie App is a straightforward and user-friendly tool for exploring movies by genre. It can be a fun and informative way to discover new films and keep your movie lists up to date. Feel free to modify and enhance the app to suit your specific needs and preferences.
