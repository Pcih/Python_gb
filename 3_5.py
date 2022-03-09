import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]



def get_jokes(number, funny_words, i):
    for i in range(number):
        
        words_1 = random.randint(0, len(nouns)-1)   
        
        funny_words.append(nouns[words_1])
        del nouns[words_1]
        words_2 = random.randint(0, len(adverbs)-1)
        funny_words.append(adverbs[words_2])
        del adverbs[words_2]
        words_3 = random.randint(0, len(adjectives)-1)
        funny_words.append(adjectives[words_3])
        del adjectives[words_3]
        # i += 1
        print(funny_words)
        funny_words = []
get_jokes(int(input('Ведите сколько шуток вы хотите но максимум 6:')), funny_words = [], i = 0)