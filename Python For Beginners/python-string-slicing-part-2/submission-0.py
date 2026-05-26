def first_n_characters(s: str, n: int) -> str:
    last_char_pos = len(s)-n
    return s[:last_char_pos]

def last_n_characters(s: str, n: int) -> str:
    first_char_pos = len(s)-n
    return s[first_char_pos]
    


# do not modify below this line
print(first_n_characters("NeetCode", 3))
print(first_n_characters("NeetCode", 4))
print(first_n_characters("NeetCode", 8))

print(last_n_characters("NeetCode", 3))
print(last_n_characters("NeetCode", 4))
print(last_n_characters("NeetCode", 8))
