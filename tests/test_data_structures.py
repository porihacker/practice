import unittest
from data_structures import *

class MyTestCase(unittest.TestCase):
    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_max([-1, 2, -3, 4, -5, 6, -9, 10]), 10)
        self.assertEqual(find_max([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), 19)

    def test_find_min(self):
        self.assertEqual(find_min([1, 2, 3, 4, 5]), 1)
        self.assertEqual(find_min([-1, 2, -3, 4, -5, 6, -9, 10]), -9)
        self.assertEqual(find_min([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -20)

    def test_find_average(self):
        self.assertEqual(find_average([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(find_average([-1, 2, -3, 4, -5, 6, -9, 10]), 0.5)
        self.assertEqual(find_average([1, -2, 3, -4, 5, -6, 9, -10, 11, -12, 13, -14, 15, -16, 17, -18, 19, -20]), -0.5)

    def test_find_all_even_numbers(self):
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5]), (2,4))
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6]), (2,4,6))
        self.assertEqual(find_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (2,4,6,8))

    def test_find_all_odd_numbers(self):
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5]), (1,3,5))
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5, 6]), (1,3,5))
        self.assertEqual(find_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]), (1,3,5,7))

    def test_find_total_number_of_even_numbers(self):
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5]), 2)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_even_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_find_total_number_of_odd_numbers(self):
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5]), 3)
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5, 6]), 3)
        self.assertEqual(find_number_of_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]), 4)

    def test_return_list_stats(self):
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5]), {
            "unique_numbers": {1, 2, 3, 4, 5},
            "min": 1,
            "max": 5,
            "average": 3.0,
            "even_numbers": (2, 4),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 2,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([1, 2, 3, 4, 5, 6]), {
            "unique_numbers": {1, 2, 3, 4, 5, 6},
            "min": 1,
            "max": 6,
            "average": 3.5,
            "even_numbers": (2, 4, 6),
            "odd_numbers": (1, 3, 5),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 3
        })
        self.assertEqual(return_list_stats([6, 2, 3, 5, 9, 4, 1, 11]), {
            "unique_numbers": {6, 2, 3, 5, 9, 4, 1, 11},
            "min": 1,
            "max": 11,
            "average": 5.1,
            "even_numbers": (6, 2, 4),
            "odd_numbers": (3, 5, 9, 1, 11),
            "number_of_even_numbers": 3,
            "number_of_odd_numbers": 5
        })

    def test_basic(self):
        input_list = ['a', '1', 'b', '3', 'c', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 3, 5])

    def test_mixed_input(self):
        input_list = ['a', '1', 'b', '3', 'c', '2', '@', '5', 'd', 'e']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(result_numbers, [1, 2, 3, 5])

    def test_repeated_characters(self):
        input_list = ['1', 'b', 'a', 'c', 'c', 'b', 'a', '1']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['a', 'b', 'c'])
        self.assertEqual(result_numbers, [1])

    def test_special_characters(self):
        input_list = ['!', '@', '#', '1', '2', '3', '$', '%', '^']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, [])
        self.assertEqual(result_numbers, [1, 2, 3])

    def test_more_special_characters(self):
        input_list = ['%', '&', '*', '4', '6', '8', '(', ')', '!', 'x']
        result_alphabets, result_numbers = process_characters(input_list)
        self.assertEqual(result_alphabets, ['x'])
        self.assertEqual(result_numbers, [4, 6, 8])

    def test_generate_squared_dict(self):
        assert generate_squared_dict(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
        assert generate_squared_dict(1) == {1: 1}
        assert generate_squared_dict(10) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
        assert generate_squared_dict(0) == {}
        assert generate_squared_dict(2) == {1: 1, 2: 4}
        assert generate_squared_dict(-5) == {-5: 25, -4: 16, -3: 9, -2: 4, -1: 1}
        assert generate_squared_dict(-1) == {-1: 1}
        assert generate_squared_dict(-10) == {-10: 100, -9: 81, -8: 64, -7: 49, -6: 36, -5: 25, -4: 16, -3: 9, -2: 4, -1: 1}
        assert generate_squared_dict(-2) == {-2: 4, -1: 1}
        assert generate_squared_dict(-3) == {-3: 9, -2: 4, -1: 1}
        assert generate_squared_dict(-6) == {-6: 36, -5: 25, -4: 16, -3: 9, -2: 4, -1: 1}


    def test_convert_word_list_sentence(self):
        words = convert_to_word_list("There is only one to fear and his name is Death,"
        +" and there is only one thing we say to Death: 'Not today!")
        self.assertEqual(['there', 'is', 'only', 'one', 'to', 'fear', 'and', 
        'his', 'name', 'is', 'death', 'and', 'there', 'is', 'only', 
        'one', 'thing', 'we', 'say', 'to', 'death', 'not', 'today'], words)

    
    def test_convert_word_list_spaces(self):
        words = convert_to_word_list("One    million    rand!")
        self.assertEqual(['one', 'million', 'rand'], words)


    def test_letters_count_sentence(self):
        char_count = letters_count_map(
            "There is only one to fear and his name is Death,"
        +" and there is only one thing we say to Death: 'Not today!")
        self.assertEqual(
            {'a': 8, 'b': 0, 'c': 0, 'd': 5, 'e': 11, 'f': 1, 'g': 1, 'h': 6, 'i': 5, 'j': 0, 'k': 0, 'l': 2, 'm': 1,
             'n': 9, 'o': 8, 'p': 0, 'q': 0, 'r': 3, 's': 5, 't': 9, 'u': 0, 'v': 0, 'w': 1, 'x': 0, 'y': 4, 'z': 0},
            char_count)
        

    def test_alphanumeric_1(self):
        self.assertEqual(text_to_morse("Hello World 123"), ".... . .-.. .-.. ---   .-- --- .-. .-.. -..   .---- ..--- ...--")
    def test_alphanumeric_2(self):
        self.assertEqual(text_to_morse(",:?!'"), "--..-- ---... ..--.. -.-.-- .----.")
    def test_alphanumeric_3(self):
        self.assertEqual(text_to_morse("Python is AWESOME!"), ".--. -.-- - .... --- -.   .. ...   .- .-- . ... --- -- . -.-.--")

