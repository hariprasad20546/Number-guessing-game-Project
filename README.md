# Number-guessing-game-Project
This is a project devoloped on python and it is about guessing a random number assumed by the computer
Number Guessing Game
The Number Guessing Game is a simple game in which the player must guess a randomly generated number between 1 and 100 within a limited number of attempts. The game is played in the command line interface and uses the Pygame and pyttsx3 libraries to play audio files and convert text to speech, respectively.

Getting Started
To get started, download, or clone the repository to your local machine. Make sure that you have Python 3 installed along with the Pygame and pyttsx3 libraries. You can install Pygame and pyttsx3 using pip with the following commands:
pip install pygame
pip install pyttsx3

Or else, go to pygame and install the packages from the library

Audio file
There will be 3 files, which improves the quality of the game, by explaning the player from start to end with a pleasent greeting.

Algorithm

1.	Initialize Pygame mixer module and create a Pyttsx3 engine object with the 'sapi5' TTS API.
2.	Set the text-to-speech engine's voice and rate properties using the Windows Registry voice ID and a rate of 125 words per minute.
3.	Define the filenames of three audio files to be used in the program.
4.	Define the play_audio function that loads an audio file, plays the audio, and waits until the audio has finished playing.
5.	Define the speak function that uses the pyttsx3 engine to convert text to speech and speaks the text.
6.	Define the generate_random_number function that generates and returns a random integer between 1 and 100, inclusive.
7.	Define the get_user_name function that prompts the user to enter their name and returns the input as a string.
8.	Define the get_user_guess function that prompts the user to enter a guess between 1 and 100 or quit, and validates the input.
9.	Define the display_message function that displays a message based on the situation and the number of tries in the game.
10.	Define the update_high_scores function that updates the list of high scores with the latest score and returns the top 5 scores.
11.	Define the display_high_scores function that prints the high scores with their respective index.
12.	Define the main function that runs the number guessing game. It initializes the high scores list, gets the user's name, and starts the game loop. If the user guesses the number correctly, the function updates the high scores and displays them. If the user quits the game, the function ends the game and thanks the player.
Within the main function:
a)	Play welcome audio files and get the user's name.
b)	Start the game loop:
I.	Generate a random number between 1 and 100 and set Number_of_tries to 0 and is_correct to False.
II.	Start the timer.
III.	While is_correct is False:
•	Get the user's guess using get_user_guess function.
•	If the user quits the game, break out of the loop and set the situation to "quit".
•	If the user guesses the number correctly, set is_correct to True and break out of the loop.
•	If the user's guess is incorrect, increment Number_of_tries by 1 and continue the loop.
IV.    End the timer and calculate the elapsed time.
V.     If the user guessed the number correctly:
•	Determine the situation and display the appropriate message using the display_message function.
•	Display the elapsed time.
•	If the situation is not "quit", update the high scores using the update_high_scores function and display the high scores using the display_high_scores function.
VI.   If the user quit the game, display a message thanking the player and end the game.
