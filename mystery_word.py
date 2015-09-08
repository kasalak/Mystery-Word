import random


def easy_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    4-6 characters.
    """
    list_easy = []

    for words in word_list:
        if 3 < len(words) < 7:
            list_easy.append(words)
    return list_easy


def medium_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    6-8 characters.
    """
    # TODO

    list_medium = []

    for words in word_list:
        if 5 < len(words) < 9:
            list_medium.append(words)
    return list_medium

def hard_words(word_list):
    """
    Returns a filtered version of the word list with words only containing
    8+ characters.
    """
    # TODO

    list_hard = []

    for words in word_list:
        if len(words) > 7:
            list_hard.append(words)
    return list_hard


def random_word(word_list):
    """
    Returns a random word from the word list.
    """
    # TODO
    return random.choice(word_list)



def display_word(word, guesses):
    """
    Returns a string that including blanks (_) and letters from the given word,
    filling in letters based upon the list of guesses.

    There should be spaces between each blank _ and each letter. Each letter
    should be capitalized for display.

    For example, if the word is BOMBARD and the letters guessed are a, b,
    and d, this function should return 'B _ _ B A _ D'.
    """
    # TODO
    display = []
    for letter in word:
        if letter in guesses:
            display.append(letter)
        else:
            display.append("_")
    display = " ".join(display).upper()
    return display


def is_word_complete(word, guesses):
    """
    Returns True if the list of guesses covers every letter in the word,
    otherwise returns False.
    """
    # TODO
    pass
    for letter in word:
        if letter not in guesses:
            return False
    return True


def main():
    """
    Runs when the program is called from the command-line.

    1. Prompts the user for a difficulty level
    2. Sets up the game based upon the difficulty level
    3. Performs the game loop, consisting of:
       a. Printing the word in progress, using _ for unguessed letters
       b. Printing the number of guesses remaining
       c. Printing the letters that have been guessed so far
       d. Prompting the user for a letter to guess
    4. Finishing the game and displaying whether the user has won or lost
    5. Giving the user the option to play again
    """
    # TODO


if __name__ == '__main__':
    main()
