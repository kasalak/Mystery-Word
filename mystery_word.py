import random



def easy_words(): # creates a list of words with 4-6 letters
    for word in word_list:

        if len(word) < 7  and len(word) > 3:
            word_bank.append(word)
    word = random.choice(word_bank)
    print("The word has {} letters".format(len(word)))

def normal_words(): # creates a list of words with 6-8 letters
    for word in word_list:

        if len(word) < 9 and len(word) > 5:
            normal_list.append(word)

    word = random.choice(word_bank)
    print("The word has {} letters".format(len(word)))


def hard_words():
    for word in word_list:

        if len(word) > 7:
            word_bank.append(word)

    word = random.choice(word_bank)
    print("The word has {} letters".format(len(word)))

def choose_difficulty():
    print("What difficulty level would you like to choose? ")
    level = input("> ")
    if "easy" in level:
        easy_words()
    elif "normal" in level:
        normal_words()
    elif "hard" in level:
        hard_words()
    else:
        print("Difficulty not chosen. Game will now exit.")

def guesses():
    letters = list(word)
    print(letters)
    wrong_guesses = []
    correct_guesses = []
    guesses_left = 8

    while guesses_left != 0:
        letter = input("Guess a letter. You have {} guesses remaining. ".format(guesses_left))

        if letter in letters:
            correct_guesses += letter
            print("Letters in word: {} The word has {} letters.".format(correct_guesses, len(word)))
        elif letter in wrong_guesses or letter in correct_guesses:
            print("You've guessed this letter before. Try again.")
        else:
            wrong_guesses += letter
            guesses_left -= 1
            print("Wrong letters guessed: {}".format(wrong_guesses))

        if len(letters) == len(correct_guesses) and guesses_left != 0:
            print("""Congratulations! You've guessed the word: {} with {} guesses left!""".format(word, guesses_left))
            break



with open('/usr/share/dict/words') as o:
    loaded_words = o.read().lower()
    word_list = loaded_words.split()
    word_bank = []

choose_difficulty()
word = random.choice(word_bank)
guesses()
