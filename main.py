__author__ = 'Semykopenko Ihor'
__version__ = 1
__status_of_task__ = 'Done'


def text_reverse(rawText: str):
    """function for reverse text and which leaves symbols and numbers in their place"""
    result = []
    symbols = set([i for i in '§±!@#$%^&*()-=_+[]{}\'"\\:;,./<>?'])
    numbers = set([i for i in '0123456789'])

    for word in rawText.split():
        # if the word have anything number or symbol
        if not str.isalpha(word):
            counter = 0
            temporary_list_for_word = []
            temporary_dict_for_symbols = {}

            for letter in word:
                if letter in symbols or letter in numbers:
                    temporary_dict_for_symbols[counter] = letter
                    counter += 1
                else:
                    counter += 1
                    temporary_list_for_word.append(letter)

            temporary_list_for_word.reverse()

            for index in temporary_dict_for_symbols:
                letter = temporary_dict_for_symbols[index]
                temporary_list_for_word.insert(index, letter)
            result.append(''.join(temporary_list_for_word))

        else:  # if the word doesn't have anything number or symbol
            result.append(word[::-1])

    return " ".join(result)


if __name__ == '__main__':

    cases = [
        ("abcd efgh", "dcba hgfe"),
        ("a1bcd efg!h", "d1cba hgf!e"),
        ("", ""),
    ]

    for text, reversed_text in cases:
        assert text_reverse(text) == reversed_text
