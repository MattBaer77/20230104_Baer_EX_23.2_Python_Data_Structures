def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

# This works, but tests return issues as tests have specific order
    # phraseSet = set(phrase)

    # phraseDict = dict.fromkeys(phraseSet, 0)
    
    # for letter in phrase:
    #     phraseDict[letter] += 1

    # return phraseDict
# This works, but tests return issues as tests have specific order

#My Solution -
    phraseDict = {}

    for letter in phrase:
        if letter in phraseDict:
            phraseDict[letter] += 1
        else:
            phraseDict[letter] = 1

    return phraseDict
#My Solution

#Suggested Solution -
    # counter = {}

    # for ltr in phrase:
    #     counter[ltr] = counter.get(ltr, 0) + 1

    # return counter
#Suggested Solution