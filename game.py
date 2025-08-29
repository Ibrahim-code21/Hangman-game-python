# Hangman Game
import random
from word_list import words

# (0-6 wrong guesses)
# It shows the hangman progressively being drawn
hangman_art =   {0:("   ",
                    "   ",
                    "   "),
                 1: (" o ", 
                     "   ",
                     "   "),
                 2: (" o ",
                     " | ",
                     "   "),
                 3: (" o ",
                     "/| ",
                     "   "),
                 4: (" o ",
                     "/|\\",
                     "   "),
                 5: (" o ",
                     "/|\\",
                     "/  "),
                 6: (" o ",
                     "/|\\",
                     "/ \\")}

def display_man(wrong_guesses):
    # Shows the hangman as the user inputs wrong guesses
    print("-------------------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-------------------------------------")

def display_hint(hint):
    # Show the word with guessed letters and underscores
    print(" ".join(hint))

def display_answer(answer):
    # Show the correct answer at the end of the game
    print(" ".join(answer))

def play_game():
    # Pick a random word for the round
    answer = random.choice(words).lower()
    # Start with underscores instead of letters
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        # Show hangman + the current guessed word
        display_man(wrong_guesses)
        display_hint(hint)
        
        # Get the player's guess
        guess = input("Enter a letter: ").lower()

        # If input is invalid (not a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("**Invalid**")
            continue

        # If player already guessed this letter
        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        # Add the letter to the guessed set
        guessed_letters.add(guess)

        # If guess is correct → reveal it in the word
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            # Wrong guess → draw more hangman
            wrong_guesses += 1

        # Check for win condition (no underscores left)
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YEAH YOU WIN!")
            is_running = False

        # Check for lose condition (if hangman is fully drawn - 6 wrong guesses the game is over)
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("DARN YOU LOST!")
            is_running = False

def main():
    # Main loop: keeps running until player says they don't want to play
    while True:
        play_game()
        again = input("Do you want to play again? press (y): ").lower()
        if again != "y":
            print("Thanks for playing Hangman!")
            break

# This makes sure the main function runs first
if __name__ == "__main__":
    main()
