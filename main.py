import random
import time
import pygame
import pyttsx3

# Initialize the Pygame mixer module and create a new Pyttsx3 engine object with the 'sapi5' text-to-speech (TTS) API
pygame.mixer.init()
engine = pyttsx3.init('sapi5')

# Sets the text-to-speech engine's voice and rate properties using the Windows Registry voice ID and a rate of 125 words per minute
voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
voices = engine.setProperty('voice', voice_id)
engine.setProperty('rate', 125)

# Define the filenames of three audio files to be used in the program
welcome_audio = "welcome.mp3"
welcome_audio1 = "welcome1.mp3"
end_audio = "thankyou.mp3"

# Loads an audio file, plays the audio, and waits until the audio has finished playing
def play_audio(audio_file):
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Uses pyttsx3 engine to convert text to speech and speaks the text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Generates and returns a random integer between 1 and 100, inclusive
def generate_random_number():
    return random.randint(1, 100)

# Prompts the user to enter their name and returns the input as a string
def get_user_name():
    return input("Enter your name: ")

# Prompts the user to enter a guess between 1 and 100 or quit, and validates the input
def get_user_guess(goal):
    while True:
        guess = input("Enter your guess between 1 to 100 or else type 'quit' to exit: ")
        if guess.lower() == "quit":
            return "quit"
        else:
            try:
                guess = int(guess)
                if guess < 1 or guess > 100:
                    print("Invalid guess. Enter a guess between 1 and 100.")
                    speak("Invalid guess. Enter a guess between 1 and 100.")
                    return False
                elif guess < goal:
                    print("it is too low")
                    speak(f"{guess} is too low, try again")
                    return False
                elif guess > goal:
                    print("It is too high!")
                    speak(f"{guess} is too high, try again")
                    return False
                else:
                    print("Great, You have found the correct answer")
                    return True
            except ValueError:
                print("Invalid input. Enter a valid guess.")
                speak("Invalid input. Enter a valid guess.")

#defines a function to display a message based on the situation and the number of tries in the game
def display_message(situation, Number_of_tries):
    if situation == "first_try" and Number_of_tries == 1:
        message = "Ohh That's awesome, you have found the number in your first try"
    elif situation == "many_attempts":
        message = f"you have taken {Number_of_tries} attempts to find the correct number."
    elif situation == "quit":
        message = "You are quitting the game before guessing the correct number."
    print(message)
    speak(message)

#This function updates the list of high scores with the latest score and returns the top 5 scores
def update_high_scores(high_scores, Number_of_tries):
    high_scores.append(Number_of_tries)
    high_scores.sort()
    return high_scores[:5]

# print the high scores with their respective index
def display_high_scores(high_scores):
    print("\nHigh Scores:")
    for index, score in enumerate(high_scores, start=1):
        print(f"{index}. {score}")

#main function that runs the number gu  essing game. It initializes the high scores list, gets the user's name, and starts the game loop. If the user guesses the number correctly, the function updates the high scores and displays them. If the user quits the game, the function ends the game and thanks the player.
def main():
    high_scores = []
    print("\nWelcome to the number guessing game!")
    play_audio(welcome_audio)
    play_audio(welcome_audio1)
    name = get_user_name()
    speak(f"Hello {name}, let's play the game!, and Now, Enter your guess between 1 to 100 or else type 'quit' to exit")
    while True:
        goal_number = generate_random_number()
        Number_of_tries = 0
        is_correct = False
        start_time = time.time()
        while not is_correct:
            is_correct = get_user_guess(goal_number)
            if is_correct == "quit":
                situation = "quit"
                break
            Number_of_tries += 1
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        if is_correct is True:
            if Number_of_tries == 1:
                situation = "first_try"
            else:
                situation = "many_attempts"
            display_message(situation, Number_of_tries)
            print(f"Elapsed time: {elapsed_time} seconds")

            if situation != "quit":
                high_scores = update_high_scores(high_scores, Number_of_tries)
                display_high_scores(high_scores)

        if situation == "quit":
            print("You quit the game before guessing the correct number.")
            speak("You quit the game before guessing the correct number.")
            play_audio(end_audio)
            print("Thank you for playing!")
            break

        speak("Do you want to play again? If yes then type yes, or else type no")
        play_again = input("\nDo you want to play again? (yes/no): ")
        if play_again.lower() == "yes":
            speak("Let's play again!")
            speak("Enter your guess between 1 to 100 or else type 'quit' to exit")
        else:
            play_audio(end_audio)
            print("Thank you for playing!")
            break
#checks if the current module is being run as the main program and then executes
if __name__ == "__main__":
    main()