#copied from hangman_helper.py
import random
POINTS_INITIAL = 10
HINT_LENGTH = 3

LETTER = 1
WORD = 2
HINT = 3

_rand = random.Random()
play_again_request = False


def set_seed(a=None):
    """
    Sets a new seed for the random generator. You don't have to use this function, but it may help you in debugging
    Search on Google for more details about the seed of random generator in python, if it interests you.
    :param a: a new seed for the random generator (an integer)
    :return: None
    """
    _rand.seed(a)


def load_words(file='words.txt'):
    """
    Loads a list of 58110 words from words.txt file
    :param file: The file of words
    :return: A list containing all the words from the file
    """
    words = []
    f_words = open(file)
    for line in f_words:
        word = line.strip()
        if(word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words


def get_random_word(words_list):
    """
    Gets a random word out of the given list of words
    :param words_list: A list of words
    :return: Some random word from the list
    """
    return _rand.choice(words_list)


def get_input():
    """
    Asks the player for his input. He can guess a letter, a word of asks for a hint.
    :return: a tuple of 2 values:
              if the player guesses a letter, returns (LETTER, letter)
              if the player guesses a word, returns (WORD, word)
              if the player asks for a hint, returns (HINT, None)
    """
    choice = input("Enter '!*' to guess a word (replace '*' with your guess), enter '?' to ask for a hint: ")
    if choice == '?':
        return HINT, None
    elif choice and choice[0]=='!':
        return WORD, choice[1:]
    return LETTER, choice


def display_state(pattern, wrong_guess_lst, points, msg):
    """
    Prints the current state of the game to the player
    :param pattern: the current pattern
    :param wrong_guess_lst: the current list of wrongs guesses
    :param points: the current amount of points the player have
    :param msg: some additional message to the player
    :return: None
    """
    print('Wrong guesses:',wrong_guess_lst)
    print('Current pattern:', " ".join(pattern))
    print('Current points:',points)
    print(msg)


def show_suggestions(matches):
    """
    Prints a list of suggestions to the player
    :param matches: a list of words
    :return: None
    """
    print('Some possible words are:')
    print(matches)


def play_again(msg):
    """
    Prints the message to the player, and gets input from him if she wants to play again.
    :param msg: The message printed to the player
    :return: True if she wants to play again, False otherwise
    """
    print(msg)
    print("Enter 'Y' or 'y' for YES, 'N' or 'n' for NO:")
    while True:
        choice = input()
        if choice and choice[0] in 'yY':
            return True
        if choice and choice[0] in 'nN':
            return False


#hangman.py

def update_word_pattern(word, pattern, letter):
    """this function returns an updated pattern containing the same letter"""
    newWord = ""
    for i in range(len(pattern)):
        if pattern[i] == word[i]:
            newWord += pattern[i]
        elif pattern[i] == '_':
            if word[i] == letter:
                newWord += letter
            else:
                newWord += '_'
    return newWord


def count_letters(word, pattern, letter):
    """how much letters the player guessed"""
    count = 0
    for i in range(len(pattern)):
        if pattern[i] == '_':
            if word[i] == letter:
                count += 1
    return count


def hintWord(words, pattern, wrong_guess_lst):
    """hint """

    lst = []
    lettters_in_pattern = []
    for char in pattern:
        if char != "_":
            lettters_in_pattern.append(char)
    for word in words:
        if len(word) == len(pattern):
            for j in range(len(words)):
                guessedWord = True
                if words[j] in wrong_guess_lst:
                    guessedWord = False
                    break
                else:
                    if pattern[j] == "_":
                        if words[j] in lettters_in_pattern:
                            guessedWord = False
                            break
                    else:
                        if pattern[j] != word[j]:
                            guessedWord = False
            if guessedWord:
                lst.append(word)
    return lst


def playerScore(word, pattern, guess):
    #check the player's score
    count = 0
    for i in range(len(pattern)):
        if pattern[i] == "_":
            count += 1
    return count


def run_single_game(words_list, score):
    """The function receives a list of words and a number of points with which
    the player starts the game and runs one game. The function returns the number
    of points the player has at the end of the game."""

    word_choose = get_random_word(words_list)
    wrongGuess = []
    pattern = ""
    for i in range(len(word_choose)):
        pattern += "_"
    display_state(pattern, wrongGuess, score, "Welcome!")

    while (score > 0) and (pattern != word_choose):
        type, data = get_input()
        if type == LETTER and 'z' >= data >= 'a' and len(data) <= 1:
            if data in pattern or data in wrongGuess:
                msg = "You wrote this letter before! Try again!"
            else:
                score -= 1
                if data in word_choose:
                    num = count_letters(word_choose, pattern, data)
                    pattern = update_word_pattern(word_choose, pattern, (data))
                    msg = "Good job!"
                    score += (num * (num + 1) // 2)
                else:
                    wrongGuess.append(data)
                    msg = "Wrong letter!"
        elif type == WORD:
            score -= 1
            if data == word_choose:
                num = playerScore(word_choose, pattern, data)
                score = score + num * (num + 1) // 2
                msg = "Wonderful!!!"
            else:
                msg = "Wrong word haha"
        elif type == HINT:
            score -= 1
            new_lst = hintWord(words_list, pattern, wrongGuess)
            new_lst2 = []
            patrn = len(new_lst)
            msg = ""
            if patrn > HINT_LENGTH:
                for index in range(1, HINT_LENGTH):
                    new_lst2.append(new_lst[(index - 1) * patrn // HINT_LENGTH])
            else:
                new_lst2 = new_lst
            show_suggestions(new_lst2)
        else:
            msg = "hmmm...couldn't find the letter"
        display_state(pattern, wrongGuess, score, msg)
    if pattern != word_choose and score == 0:
        msg = "You loose! the word was " + str(word_choose)
    else:
        msg = "You won, congrats!"
    display_state(pattern, wrongGuess, score, msg)
    return score
