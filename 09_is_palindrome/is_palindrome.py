def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    #My Solution
    phrase_ignore = phrase.lower().replace(" ", "")
    phrase_reversed = phrase_ignore[::-1]

    if phrase_ignore == phrase_reversed:
        return True
    else:
        return False
    #My Solution

    #Suggested Solution
    # normalized = phrase.lower().replace(' ', '')
    # return normalized == normalized[::-1]
    #Suggested Solution
