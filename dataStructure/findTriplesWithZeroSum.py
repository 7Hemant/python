"""
Given a list of integers, return element a,b,c such that  a+b+c=0

    Args:
       nums: list of integers 
    Returns:
       list of lists of integer where sum(each_list) ==0
    

run code :  python -m doctest -v findTriplesWithZeroSum.py              
 
"""

from itertools import combinations

def find_triple_with_0_sum(nums: list[int]) -> list[list[int]]:
    """
    Examples:
    >>> find_triple_with_0_sum([0, 0, 0])
    [[0, 0, 0]]
    """
    return [
        list(x)
        for x in sorted({abc for abc in combinations(sorted(nums), 3) if not sum(abc)})
    ]

if __name__ == "__main__":
    import doctest

    doctest.testmod()
