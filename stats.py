
def count_words(text):
    return len(text.split())

def count_chars(text):
    res = {}
    for char in text:
        char = char.lower()
        res[char] = res.get(char, 0) + 1
    return res

def sort_chars(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)
