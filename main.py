__author__ = 'Semykopenko Ihor'
__version__ = 2
__status_of_task__ = 'Done'


def rules() -> list:
    """creator of rules on the foundation the signs and numbers"""
    numbers = [i for i in '0123456789']
    sings = [i for i in '§±!@#$%^&*()-=_+[]{}\'"\\:;,./<>?']
    return numbers + sings


def alphabet() -> list:
    """creator of alphabet in ASCII"""
    lowercase = [chr(letter) for letter in range(97, 123)]  # letters in lowercase
    uppercase = [chr(letter) for letter in range(65, 91)]  # letters in uppercase
    return uppercase + lowercase


def check_in_the_rules(word: str) -> bool: return bool(list(filter(lambda x: x in rules(), word)))


def reverse_word_with_rules(rawWord: str) -> list:
    # "a1bcd" -> "d1cba" - should be
    # rawWord[::-1] = "dcb1a"

    raw_result = []

    enumerate = 0



    for letter in rawWord[::-1]:
        print(f'L: {letter}  RE: {rawWord[enumerate]}')
        if rawWord[0] in rules():
            symbol_last = rawWord[0]

        if rawWord[enumerate] in rules():
            raw_result.append(rawWord[enumerate])
            raw_result.append(letter)
            enumerate += 1

        elif letter in rules():
            continue

        elif letter in alphabet():
            raw_result.append(letter)
            enumerate += 1
    return raw_result


def reverse_word(rawWord: str) -> str:
    """this function return word in reverse in the selected rules"""

    # if the word have anything number or symbol
    if check_in_the_rules(word=rawWord):
        return ''.join(reverse_word_with_rules(rawWord=rawWord))
        # reverse_word_with_rules(rawWord=rawWord)
        # return 'qweqw'
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
        ("a1bcd  efg!h", "d1cba  hgf!e"),  # I have two "space" in the text
        ("", ""),
        ("Hello World!", "olleH dlroW!")
    ]

    for text, reversed_text in cases:
        # assert text_reverse(text) == reversed_text
        print(text_reverse(text) == reversed_text)

    # print(text_reverse('World!'))