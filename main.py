__author__ = 'Semykopenko Ihor'
__version__ = 4
__status_of_task__ = 'Done'


rules = '0123456789' + '§±!@#$%^&*()-=_+[]{}\'"\\:;,./<>?'
alphabet = [chr(letter) for letter in range(97, 123)] + [chr(letter) for letter in range(65, 91)]


def check_in_the_rules(word: str) -> bool: return any(char for char in word if char in rules)


def reverse_word_with_rules(word: str) -> list:
    """function for reversing word with rules"""
    result = []
    zip_symbols = {index: char for index, char in enumerate(word) if char in rules}
    cleared_word = [char for char in word if char in alphabet]  # cleared text which found in alphabets
    for index, letter in enumerate(word):
        if index in zip_symbols:
            result.append(letter)
        else:
            result.append(cleared_word.pop())
    return result


def reverse_word(rawWord: str) -> str:
    """this function return word in reverse in the selected rules"""
    #  if the word have anything number or symbol
    if check_in_the_rules(word=rawWord):
        return ''.join(reverse_word_with_rules(word=rawWord))
    else:  # if the word doesn't have anything number or symbol
        return ''.join(list(rawWord)[::-1])


def text_reverse(Text: str):
    """function for reverse text and which leaves symbols and numbers in their place"""
    # getting list of word, with separator " " - space | exp: 'hello world' -> ['hello', 'world']
    return ' '.join([reverse_word(word) for word in Text.split(' ')])


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
        ("pyth123@on", "noht123@yp"),
        ("ab123", "ba123")

    ]

    for text, reversed_text in cases:
        assert text_reverse(text) == reversed_text

