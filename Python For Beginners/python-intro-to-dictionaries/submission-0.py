from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    dict_1 = {
        name : age
    }
    return dict_1


def list_to_dict(words: List[str]) -> Dict[str, int]:
    dict_2 = {}
    for i in range(len(words)):
        dict_2[i] = words[i]
    return dict_2



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
