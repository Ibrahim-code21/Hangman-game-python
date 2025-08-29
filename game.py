import random
from word_list import words


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
    print("-------------------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-------------------------------------")

def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def play_game():
    answer = random.choice(words).lower()
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("**Invalid**")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YEAH YOU WIN!")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("DARN YOU LOST!")
            is_running = False

def main():
    while True:
        play_game()
        again = input("Do you want to play again? press (y): ").lower()
        if again != "y":
            print("Thanks for playing Hangman!")
            break


if __name__ == "__main__":
    main()
