# Done
def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = list('aeiouAEIOU')
    lst = list(s)
    onlyvowels = [ch for ch in lst if ch in vowels]
    vi = len(onlyvowels) - 1
    if len(onlyvowels) == 0:
        return s
    for i in range(len(lst)):
        if lst[i] in vowels:
            lst[i] = onlyvowels[vi]
            vi -= 1
    return ''.join(lst)