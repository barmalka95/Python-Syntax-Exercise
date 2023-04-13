def print_upper_words(words):
    """will print every word on a separate line and turn it into uppercase """

    for word in words:
        print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])


def print_upper_words2(words):
    """will print only words that starts with e or E"""
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


print_upper_words2(["hello", "hey", "goodbye", "yo", "yes", "e", "E"])


def print_upper_words3(words, must_start_with):
    """will print only words that starts with the letters we put in must_start_with argument"""
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words3(["hello", "hey", "goodbye", "yo", "yes", "e", "t", "E"],
                   must_start_with={"h", "y"})
