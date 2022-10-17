__author__ = 'Semykopenko Ihor'
__version__ = 4
__status_of_task__ = 'Done'


def rules_function() -> list:
    """creator of rules on the foundation the signs and numbers"""
    numbers = [i for i in '0123456789']
    sings = [i for i in '§±!@#$%^&*()-=_+[]{}\'"\\:;,./<>?']
    return numbers + sings


def alphabet_function() -> list:
    """creator of alphabet in ASCII"""
    lowercase = [chr(letter) for letter in range(97, 123)]  # letters in lowercase
    uppercase = [chr(letter) for letter in range(65, 91)]  # letters in uppercase
    return uppercase + lowercase


rules = rules_function()
alphabet = alphabet_function()
def check_in_the_rules(word: str) -> bool: return bool(list(filter(lambda x: x in rules, word)))


def reverse_word_with_rules(rawWord: str) -> list:
    """function for reversing word with rules"""
    result = []
    length_of_string = len(rawWord)  # length of string
    zip_symbols = dict(filter(lambda x: x[1] in rules, zip(range(len(rawWord)), list(rawWord))))  # indexing characters
    cleared_reverse_word = list(filter(lambda x: x in alphabet, rawWord))  # cleared text which found in alphabets
    list_word_keys = list(zip_symbols.keys())[::-1]  # reversed index's - characters

    for index in range(length_of_string):
        if index in list_word_keys:
            result.append(zip_symbols[index])
        else:
            result.append(cleared_reverse_word.pop())
    return result


def reverse_word(rawWord: str) -> str:
    """this function return word in reverse in the selected rules"""
    #  if the word have anything number or symbol
    if check_in_the_rules(word=rawWord):
        return ''.join(reverse_word_with_rules(rawWord=rawWord))
    else:  # if the word doesn't have anything number or symbol
        return ''.join(list(rawWord)[::-1])


def text_reverse(rawText: str):
    """function for reverse text and which leaves symbols and numbers in their place"""
    # getting list of word, with separator " " - space | exp: 'hello world' -> ['hello', 'world']
    words = rawText.split(' ')

    raw_result = []
    for word in words:
        raw_result.append(reverse_word(word))
    return ' '.join(raw_result)


if __name__ == '__main__':

    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),

        # <-- My additions -->
        ("a1bcd  efg!h", "d1cba  hgf!e"),  # I have two "space" in the text
        ("   ", "   "),
        ("Hello World!", "olleH dlroW!"),
        ("!Hello World", "!olleH dlroW"),
        ("x!x", "x!x"),
        ("pyth123@on", "noht123@yp")

    ]

    for text, reversed_text in cases:
        assert text_reverse(text) == reversed_text
        print(text_reverse(text) == reversed_text)


