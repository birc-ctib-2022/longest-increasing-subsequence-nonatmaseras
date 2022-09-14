"""Module for computing the longest increasing subsequence."""

from typing import Sequence, Any


def is_increasing(x: Sequence[Any]) -> bool:
    """
    Determine if x is an increasing sequence.

    >>> is_increasing([1, 4, 6])
    True
    >>> is_increasing("abc")
    True
    >>> is_increasing("cba")
    False
    """
    for i in range(len(x) - 1):
        if not x[i] < x[i+1]:
            return False
    return True


def liseq(x: Sequence[Any]) -> list[int]:
    """
    Compute a longest increasing subsequence.

    Return the sequence as a list of indices.

    >>> liseq([12, 45, 32, 65, 78, 23, 35, 45, 57])
    [0, 5, 6, 7, 8]
    """
    best: list[int] = []
    
    if len(x) == 0: ## base case
        return []
    
    min_len = 1 ##at least 1 number in the solution subset
    indices = [None] * len(x)  # the max possible solution has the length of X 
    indices[0] = 0 ## set first index as 0

    for i in range(1, len(x)):
        lower = 0
        upper = min_len # first upper boundary is the 2n number
        #first iteration: first number < second number
        if x[indices[upper-1]] < x[i]: 
            #if it is, new upper bound
            j = upper

        else:
            # binary search (~ kind of)
            #if the next number is smaller AND the indices are non-consecutive
            #   : is any of the numbers before the new upper limit smaller? -> update boundaries
            
            #print("IT " + str(i))
            while upper - lower > 1:
                half = (upper + lower) // 2
                check_position = x[indices[half-1]]
                #print("UPPER " + str(upper), end = ' ')
                #print("LOWER "+ str(lower),end= ' ')
                #print("POSITION TO CHECK: " + str(check_position), end = ' ')
                if  check_position < x[i]:
                    lower = half
                else:
                    upper = half
                #print("NEW UPPER " + str(upper), end = ' ')
                #print("NEW LOWER "+ str(lower))

            j = lower #update the upper boundary with the position of the small value 

        ##if we are comparing the next number OR 
        # we have set a new upper boundary including an increasing set
        if j == min_len or x[i] < x[indices[j]]:
            indices[j] = i
            ## set the next iteration upper boundary: go to the next position (j+1)
            min_len = max(min_len, j+1)  
        
    return [x for x in indices if x is not None] #best  


