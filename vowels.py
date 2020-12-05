import re
import unittest

vowel_pattern = r"[AaUuEeOoYyIi]"

def count_vowels(word):
    count = 0
    for match in re.finditer(vowel_pattern, word):
        count += 1
    
    return count


class TestCountVowels(unittest.TestCase):
    def test_no_vowels(self):
        self.assertEqual(0, count_vowels("przm"))

    def test_one_vowel(self):
        self.assertEqual(1, count_vowels("cat"))
    
    def test_two_vowels(self):
        self.assertEqual(2, count_vowels("hey"))


if __name__ == '__main__':
    unittest.main()