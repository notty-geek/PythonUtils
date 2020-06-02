def split_list(l: list, parts: int) -> list:
    """Takes a list as input, and splits it into "parts" number of sub-lists,
    which are then inserted as elements in the returned meta-list.
    
    The function will try to make the sub-lists as equal in length as 
    possible, so running
    split_list( [1, 2, 3, 4, 5, 6], 4 ) 
    will return 
    [ [1, 2], [3, 4], [5], [6] ]
    
    I will also make sure that the list isn't split into more parts than
    there are elements in the list, so
    split_list( [a, b], 6 ) 
    will return 
    [ [a], [b] ]
    """
    n = min(parts, max(len(l),1))
    k, m = divmod(len(l), n)
    return [l[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(n)]
