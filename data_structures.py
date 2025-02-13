import random
import re
import string


def odds_even(numbers, return_type="even"):
    even = []
    odds = []
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
        else:
            odds.append(number)

    if return_type == "even":
        return even
    elif return_type == "odds":
        return odds
    else:
        raise ValueError("return_type must be odd or even")


def find_extreme(numbers, return_type="max"):

    if return_type == "max":
        return max(numbers)
    elif return_type == "min":
        return min(numbers)
    elif return_type == "average":
        return round(sum(numbers) / len(numbers), 1)


def generate_random_list(length):
    """Generate a list of random numbers of a given length"""
    random_list = []
    for i in range(length + 1):
        number = random.random()
        random_list.append(number)
    return random_list


def find_max(numbers):
    """Find the maximum number in a list of numbers"""
    return find_extreme(numbers, "max")


def find_min(numbers):
    """Find the minimum number in a list of numbers"""

    return find_extreme(numbers, "min")


def find_average(numbers):
    """Find the average of a list of numbers"""

    return find_extreme(numbers, "average")


def find_number_of_even_numbers(numbers):
    """Find the number of even numbers in a list of numbers"""

    return len(odds_even(numbers, "even"))


def find_number_of_odd_numbers(numbers):
    """Find the number of odd numbers in a list of numbers"""
    return len(odds_even(numbers, "odds"))


def find_even_numbers(numbers):
    """Find the number of even numbers in a list of numbers"""
    list_even = odds_even(numbers, "even")
    return tuple(list_even)


def find_odd_numbers(numbers):
    """Find the number of odd numbers in a list of numbers"""

    list_odds = odds_even(numbers, "odds")

    return tuple(list_odds)


def return_list_stats(the_list):
    """Return a dictionary containing the max, min, mean, and average of a list of numbers"""

    return {
        "unique_numbers": set(the_list),
        "max": find_max(the_list),
        "min": find_min(the_list),
        "average": find_average(the_list),
        "even_numbers": find_even_numbers(the_list),
        "odd_numbers": find_odd_numbers(the_list),
        "number_of_even_numbers": find_number_of_even_numbers(the_list),
        "number_of_odd_numbers": find_number_of_odd_numbers(the_list),
    }


def process_characters(input_list):
    """
    Process a list of characters, separating alphabets and numbers,
    removing duplicates and returning them in sorted order.

    Parameters:
    - input_list (list): A list containing characters.

    Returns:
    - Two lists - sorted alphabets as strings and sorted numbers as integers.
    """

    # numbers = [x for x in input_list if x.isdigit()]
    # alpha = [x for x in input_list if x.isalpha()]

    # return list(sorted(set(alpha))), list(
    #     sorted(set(int(number) for number in numbers))
    # )
    numbers = [x for x in input_list if x.isdigit()]
    alpha = [x for x in input_list if x.isalpha()]

    return list(sorted(set(alpha))), list(sorted(set(int(x) for x in numbers)))


def generate_squared_dict(n):
    """
    Generate a dictionary containing numbers and their squares.

    Given a positive integer `n`, this function will generate a dictionary
    that contains numbers from 1 to n as keys and their squares as values.

    Parameters:
        n (int): The upper limit for the numbers in the dictionary.

    Returns:
        dict: A dictionary with numbers and their squares.

    Example:
        >>> generate_squared_dict(5)
        {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
    """
    square_dict = {}
    if n > 0:

        for number in range(1, n + 1):
            square_dict[number] = number**2
    elif n < 0:

        for number in range(n, 0):
            square_dict[number] = number**2

    return square_dict


def split(delimiters, text):
    """
    Helper function.
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """
    regex_pattern = "|".join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def get_delimiters(text):
    """
    Helper function.
    This function serves as an option to use to obtain delimiters.
    """
    set_del = {word for word in text if word in string.punctuation}
    delimiters = list(set_del)
    delimiters = "".join(delimiters) + " "
    return delimiters


def convert_to_word_list(text):
    """
    Returns all words in a sentence as a list without the punctuation and spaces.
    :param text: Input text to convert to word list
    :return: List of lowercase words with punctuation removed
    """
    # lst = []

    # for i in split(get_delimiters(text), text):
    #     if i.lower() != "":
    #         lst.append(i.lower())
    # return lst

    # lst = []
    # for i in split(get_delimiters(text), text):
    #     if i.lower() != "":
    #         lst.append(i.lower())
    # return lst
    LST=[]
    

def letters_count_map(text):
    """
    Map the total count of each letter to the alphabet and return this as a dictionary.
    """
    # full_dict = {letter: 0 for letter in string.ascii_lowercase}

    # for char in text.lower():
    #     if char.isalpha():
    #         full_dict[char] += 1

    # return full_dict
    full_dict = {letter: 0 for letter in string.ascii_lowercase}

    for char in text.lower():
        if char.isalpha():
            full_dict[char] += 1
    return full_dict


def text_to_morse(text):
    """
    Convert a given string to its Morse code equivalent.

    The function takes an input string containing alphanumeric characters in lower or upper case,
    along with special characters that are handled in Morse code, including commas, colons, apostrophes,
    periods, exclamation marks, and question marks. It returns the Morse code representation of the input string.

    Parameters:
        text (str): The input string to be converted to Morse code.

    Returns:
        str: The Morse code representation of the input string.

    Morse Code Mapping:
        Alphanumeric characters (case-insensitive) and digits 0-9 are mapped to their respective Morse code representations.
        Special characters are also handled accordingly as follows:
            ',' (comma) : '--..--'
            ':' (colon) : '---...'
            "'" (apostrophe) : '.----.'
            '.' (period) : '.-.-.-'
            '!' (exclamation mark) : '-.-.--'
            '?' (question mark) : '..--..'
            Space (' ') : ' '

    Examples:
        >>> text_to_morse("Hello World 123")
        '.... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...-- '
    """
    morse_code_dict = {
        "A": ".-",
        "B": "-...",
        "C": "-.-.",
        "D": "-..",
        "E": ".",
        "F": "..-.",
        "G": "--.",
        "H": "....",
        "I": "..",
        "J": ".---",
        "K": "-.-",
        "L": ".-..",
        "M": "--",
        "N": "-.",
        "O": "---",
        "P": ".--.",
        "Q": "--.-",
        "R": ".-.",
        "S": "...",
        "T": "-",
        "U": "..-",
        "V": "...-",
        "W": ".--",
        "X": "-..-",
        "Y": "-.--",
        "Z": "--..",
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        ",": "--..--",
        ":": "---...",
        "'": ".----.",
        ".": ".-.-.-",
        "!": "-.-.--",
        "?": "..--..",
        " ": " ",
    }
    # words = text.split()
    # morse_words = []
    # for word in words:
    #     current_word = []
    #     for char in word:
    #         if char.isalpha():
    #             upper_char = char.upper()
    #             code = morse_code_dict.get(upper_char, "")
    #         else:
    #             code = morse_code_dict.get(char, "")
    #         if code:
    #             current_word.append(code)
    #     morse_words.append(" ".join(current_word))
    # return "   ".join(morse_words)
    new_string = ""
    for i in text:
        if i.isalpha():
            new_string += morse_code_dict[i.upper()]
        else:
            new_string += morse_code_dict[i]
        new_string += " "
    return new_string.strip()
