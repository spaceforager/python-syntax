def print_upper_words(words):
    """Given list of words, prints each word on a separate line in all uppercase."""

    # YOUR CODE HERE
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e.

       >>> print_upper_words2(["eagle", "Edward", "Alfred"])
       EAGLE
       EDWARD
   """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break


print_upper_words(['apple', 'banana', 'orange', 'pineapple', 'mango'])
print_upper_words2(["eagle", "Edward", "Alfred"])
print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
                   must_start_with=["A", "E"])
