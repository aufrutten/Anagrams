__author__ = 'Semykopenko Ihor'
__version__ = 3
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
    # "a1bcd" -> "d1cba" - should be
    # rawWord[::-1] = "dcb1a"

    raw_result = []
    last_symbol = None
    enumerate = 0  # index for rawWord[::-1]

    # iteration of word in reverse mode
    for letter in rawWord[::-1]:
        if letter in rules and enumerate == 0:  # exception when first letter exist in rules
            last_symbol = letter

        if rawWord[enumerate] in rules:  # checking if letter in rawWord exist in rules
            raw_result.append(rawWord[enumerate])  # adding our exception
            if letter not in rules:  # checking if letter not in rules
                raw_result.append(letter)  # adding
            enumerate += 1

        elif letter in rules:
            continue

        elif letter in alphabet:
            raw_result.append(letter)
            enumerate += 1

    if last_symbol is not None:
        raw_result.append(last_symbol)

    return raw_result


def reverse_word(rawWord: str) -> str:
    """this function return word in reverse in the selected rules"""

    # if the word have anything number or symbol
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

        ("a1bcd  efg!h", "d1cba  hgf!e"),  # I have two "space" in the text
        ("   ", "   "),
        ("Hello World!", "olleH dlroW!"),
        ("!Hello World", "!olleH dlroW"),
        ("x!x", "x!x"),
    ]

    for text, reversed_text in cases:
        assert text_reverse(text) == reversed_text
        print(text_reverse(text) == reversed_text)
