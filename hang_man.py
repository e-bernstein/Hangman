from class_word import class_word
from functions_hangman import game, read_text

#type 'random' for random word
#guess 'zupf' for all time win
#type 'stop' at 'press enter' to quit

if __name__ == '__main__':
    ki_words = read_text()
    
    test = class_word()
    game(test, ki_words, [])