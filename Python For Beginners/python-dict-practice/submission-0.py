from typing import Dict # this adds type hinting for Dict

def count_characters(word: str) -> Dict[str, int]:
    word_count = {}
    for char in word:
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1
    return word_count




# don't modify below this line
print(count_characters("hello"))
print(count_characters("world"))
print(count_characters("hello world"))
print(count_characters("this is a longer sentence"))
