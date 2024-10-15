"""
Given a sequence arr[] of size n,  this is function return 
an equilibrium  index( if any) or - 1 if no equilibrium  index exits.

The equilibrium index of an array is an index such that the sum of element 
at lower indexes is equal to the sum of element at higher indexs.

example 

input =[1,2,3,4,5]
output = -1

input =[1,1,1,1,1]
output = 2 # indexvalue 

to run this programming use this command "python -m doctest -v EquilibriumIndexInArray.py"
"""


def equilibrium_index(arr:list[int])->int:
    """
    examples ::
    >>> equilibrium_index([1,1,1,1,1])
    2

    >>> equilibrium_index([4,1,2,2])
    1

    >>> equilibrium_index([4,2,3,2])
    -1

    """ 
    total_sum = sum(arr)
    left_sum = 0

    for i,value in enumerate(arr):
        total_sum-=value
        if left_sum == total_sum:
            return i
        left_sum += value 

    return -1

if __name__ == "__main__":
    import doctest

    doctest.testmod()


