def remove_fourth_character(word: str) -> str:
    if len(word) > 4:
        first_half_string = word[:3]
        second_half_string = word[4:]
        return first_half_string + second_half_string
    elif len(word) == 4:
        return word[:3]
    else:
        return ''
#Hell

# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
