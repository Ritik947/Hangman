import string
from typing import Counter
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    if set(Counter(secret_word).keys()).issubset(set(Counter(letters_guessed).keys())):
        return True
    return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(available_letters, letter_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = available_letters
    letters_left = letters_left.replace(letter_guessed,"")
    return letters_left

def get_hint(secret_word, letters_guessed):
    for c in secret_word:
        if c not in letters_guessed:
            return c

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')
    remaining_lives = 8
    available_letters = string.ascii_lowercase
    letters_guessed = []
    hint = True
    n = len(secret_word)
    while remaining_lives > 0:
        letter = input("Please guess a letter: ")
        if letter == "help":
            if hint:
                hint = False
                letter = get_hint(secret_word, letters_guessed)
            else:
                print("Hint already used")
                continue
        if not (letter in string.ascii_lowercase and len(letter)==1):
            print("Invalid input! Try again")
            continue
        available_letters = get_available_letters(available_letters, letter)
        print("Available letters: {} ".format(available_letters))
        if letter in secret_word:
            letters_guessed.append(letter)
            print("Good guess: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            if is_word_guessed(secret_word, letters_guessed) == True:
                print(" * * Congratulations, you won! * * ", end='\n\n')
                break
        else:
            print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
            remaining_lives-=1
            if remaining_lives == 0:
                print("GAME OVER! You are out of lives")
                print(IMAGES[-2])
                break
            else:
                print("Lives remaining: ", remaining_lives)
                print(IMAGES[8-remaining_lives-1])
            letters_guessed.append(letter)
            print("")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
