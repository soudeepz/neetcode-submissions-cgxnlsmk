def remove_fourth_character(word: str) -> str:
    if len(word) > 4:
        first_half_string = word[:4]
        second_half_string = word[5:]
        return first_half_string + second_half_string
    elif len(word) == 4:
        return word[:4]

    else:
        return ''


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
