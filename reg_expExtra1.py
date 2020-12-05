import re
from vowels import count_vowels

sentence_pattern = r"(\.|^)((\W*\b)\w+(\W*\b)){6}\."
word_pattern = r"\w+"


def is_sentence_valid(sentence):
    for word_match in re.finditer(word_pattern, sentence):
        word = word_match.group(0)
        vowel_count = count_vowels(word.strip())
        if (vowel_count >= 2):
            return True
            
with open("Macbeth.txt") as file:
    text = file.read()
    
    for sentence_match in re.finditer(sentence_pattern, text):
        sentence = sentence_match.group(0)
        
        # часть ответственная за поиск двусложного слова в предложении
        if is_sentence_valid(sentence):
            print(sentence)
        


