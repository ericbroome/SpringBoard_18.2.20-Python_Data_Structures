# Done
def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """

    def countItems(lst):
        """
            Count the instances of items in a list
        """
        # Make
        result = dict.fromkeys(set(lst), 0)
        for n in lst:
            result[n] += 1
        return result

    return countItems(str(num1)) == countItems(str(num2))