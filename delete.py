import string
import re

new_stuff = "There is only one to fear and his name is Death, and there is only one thing we say to Death: 'Not today!"

# Initialize a dictionary with all letters from a to z
# full_dict = {letter: 0 for letter in string.ascii_lowercase}
# full_dict={letter:0 for letter in string.ascii_lowercase}
import re
import string


def split(delimiters, text):
    """
    Helper function.
    Splits a string using all the delimiters supplied as input string
    :param delimiters: string containing delimiters to use to split the string, e.g. `,;? `
    :param text: The input text to be split
    :return: a list of words from splitting text using the delimiters
    """
    regex_pattern = "|".join(map(re.escape, delimiters))
    return re.split(regex_pattern, text)


def get_delimiters(text):
    """
    Helper function.
    This function obtains all punctuation characters present in the text.
    :param text: Input text to extract delimiters from
    :return: String of unique delimiters including space
    """
    set_del = {char for char in text if char in string.punctuation}
    delimiters = "".join(set_del) + " "
    return delimiters


def convert_to_word_list(text):
    """
    Returns all words in a sentence as a list without the punctuation and spaces.
    :param text: Input text to convert to word list
    :return: List of lowercase words with punctuation removed
    """
    # First remove punctuation
    # First get all delimiters from the text
    delimiters = get_delimiters(text)
    # Then use these delimiters to split the text
    return split(delimiters, text)


# Example usage
text = "Hello, world! How are you today? Let's split this text."
word_list = convert_to_word_list(text)
print(word_list)
