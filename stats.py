

def count_words(content):
    number_of_words = len(content.split())
    return number_of_words


def count_char(content):
    characters = {}
    for char in content:
        char = char.lower()
        if char in characters:
            characters[char] +=1 
        else:
            characters[char] = 1
    return characters



