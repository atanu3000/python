import random
import hangman_art
import hangman_words
# word_list = ["ardvark", "baboon", "camel"]
choosen_word = random.choice(hangman_words.word_list)
print(hangman_art.logo)
print("The solution is " + choosen_word)
lives = 6
display = []
for _ in range(len(choosen_word)):
    display += "_"
# print(display)

end_of_game = False
while not end_of_game:
    guess = input("Guess a word: ").lower()

    for possition in range(len(choosen_word)):
        letter = choosen_word[possition]
        if letter == guess:
            display[possition] = letter

    
    if guess not in choosen_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You Win!")
