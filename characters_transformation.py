def replace_letters(word):
    alphabet = {
        "a": "z", "b": "e", "c": "e", "d": "e", "e": "d",
        "f": "i", "g": "i", "h": "i", "i": "h", "j": "o",
        "k": "o", "l": "o", "m": "o", "n": "o", "o": "n",
        "p": "u", "q": "u", "r": "u", "s": "u", "t": "u",
        "u": "t", "v": "a", "w": "a", "x": "a", "y": "a",
        "z": "a",
    }

    replaced_word = ""

    for char in word:
        replaced_word += alphabet[char]

    return replaced_word


def test_replace_letters():
    assert replace_letters("cat") == "ezu"
    assert replace_letters("codewars") == "enedazuu"
    assert replace_letters("hello") == "idoon"
    assert replace_letters("world") == "anuoe"
    assert replace_letters("abracadabra") == "zeuzezezeuz"


test_replace_letters()
