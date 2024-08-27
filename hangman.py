import random
from hangman_words import words_list
from hangman_art import stages, logo

lives = 6

print (logo)

chosen_word = random.choice(words_list)


placeholder = ""

word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"

print(placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"*** {lives}/6 LIVES LEFT ***")

    guess = input("Guess a letter: ").lower()
    print(guess)

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    if guess not in chosen_word:
        lives -= 1
        print (f"You guessed {guess}, that's not in the word. You lose a life. ")
        if lives == 0:
            game_over = True
            print (f"It was {chosen_word}. You lose.")

    if "_" not in display:
        game_over = True
        print ("You win.")
    
    print(stages[lives])