import re;


text = "А ты знал, что ВТ – лучшая кафедра в ИТМО?"
phrase_pattern = "ВТ(\W+\w+){,3}\W+ИТМО"
word_pattern = "\w+"

def proga():
    phrase = re.search(phrase_pattern, text)
    result = re.findall(word_pattern, phrase.group(0)) 
    string = ""
    for word in result:
        string += word + " "
    print(string)    

proga()    