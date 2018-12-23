def search4vowels(phrase: str) -> set:
    """Displays vowels found in the word given as an argument."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str='aeiou') -> set:
    """Returns a set of searched letters found in the phrase."""
    return set(letters).intersection(set(phrase))
