def num_of_words(text):
    words = text.split()
    return len(words)

def character_count(text):
    dict = {}
    lowercase = text.lower()
    for char in lowercase:
        if char not in dict:
            dict[char] = 0
        dict[char] += 1
    return dict

def sorted_char(dict):
    list = []
    for char, count in dict.items():
        if char.isalpha():
            list.append({"char": char, "num": count})
    list.sort(reverse=True, key=lambda x: x["num"])
    return list