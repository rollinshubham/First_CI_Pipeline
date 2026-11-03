
def is_anagram(first, second):
    # Remove spaces and convert to lowercase
    first = first.replace(" ", "").lower()
    second = second.replace(" ", "").lower()

    # Check whether both strings contain the same letters
    return sorted(first) == sorted(second)
