import string

SCORES_OF_LETTERS = {letter: ord(letter) - 96 for letter in string.ascii_letters}


def _score(word):
    global SCORES_OF_LETTERS

    return sum(map(lambda x: SCORES_OF_LETTERS[x], word))


def high(x):
    highest_scoring_word = ''
    max_score = -1

    for word in x.split():
        curr_score = _score(word)
        if curr_score > max_score:
            max_score = curr_score
            highest_scoring_word = word
    return highest_scoring_word
    # or use max function with key param
    # return max(x.split(), key=lambda word: sum([ord(ch) - 96 for ch in word]))