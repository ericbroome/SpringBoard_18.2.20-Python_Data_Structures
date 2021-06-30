# Done
def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

# list_manipulation(lst, command, location, value=None)
    loc = {"beginning": 0, "end": len(lst)}
    command = command.strip().lower()
    location = loc.get(location.strip().lower(), None)
    if(location == None):
        return None

# remove: remove item at beginning or end, and return item removed
    if (command == 'remove'):
        if(location > 0): location = -1
        return lst.pop(location)

# add: add item at beginning/end, and return list
    if(command == 'add'):
        if value is None: return None
        lst.insert(location, value)
        return lst

# Invalid command - return None        
    return None