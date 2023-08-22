import random


def hide_word(word, guessed_letters):
    hidden = ""
    for letter in word:
        if letter in guessed_letters:
            hidden += letter
        else:
            hidden += "*"
    return hidden


def main_fun():
    fruits = ["apple", "banana", "cherry", "orange", "grape", "strawberry"]
    selected_word = random.choice(fruits)
    attempts = int(input("Enter the number of attempts: "))
    guessed_letters = []

    print("Welcome to the Game 'Guess the FRUIT'!!!")
    print(hide_word(selected_word, guessed_letters))

    while attempts > 0:
        guess = input("Enter a letter or the full word: ").lower()

        if guess == selected_word:
            print("Congratulations, you've guessed the word!")
            break
        elif len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You've already guessed this letter.")
            elif guess in selected_word:
                guessed_letters.append(guess)
                hidden_word = hide_word(selected_word, guessed_letters)
                print(hidden_word)
                if hidden_word == selected_word:
                    print("Congratulations, you've guessed the word!")
                    break
            else:
                attempts -= 1
                print("No such letter in the word. Attempts left:", attempts)
        else:
            print("Please enter a single letter or the full word.")

    if attempts == 0:
        print("Sorry, you have no more attempts. Hidden word was:", selected_word)


if __name__ == "__main__":
    main_fun()
