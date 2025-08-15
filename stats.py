
    
def get_word_count(text):
    return len(text.split())

def get_frequencies(text):
    
    frequencies = {}
    for word in text:
        if word.lower() in frequencies:
            frequencies[word.lower()] += 1
        else:
            frequencies[word.lower()] = 1
    return frequencies

def get_only_character_frequency(words):
    frequencies = {}
    for word in words:
        if word.isalpha():
            if word.lower() in frequencies:
                frequencies[word.lower()] += 1
            else:
                frequencies[word.lower()] = 1
    return frequencies

def get_frequency_list(words):
    frequency_list = []
    frequencies = get_only_character_frequency(words)
    for word in frequencies:
        frequency_list.append({"word": word, "count": frequencies[word]})
    return frequency_list