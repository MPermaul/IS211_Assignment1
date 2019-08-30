def listDivide (numbers, divide = 2):
    '''Function that takes in list numbers and returns how many items are divisible by divide.
    Arguments:
        numbers (list):     Arg for a list that's passed in.
        divide (int):       Arg for the value used to divide the list items by. Default is 2.
    
    Return:
        num_divisible (int):    The number of elements in list that are divisible by divide.

    Example:
        >>> listDivide([1,2,3,4,5])
        >>> 2

        >>> listDivide([30,54,63,98,100], divide=10)
        >>> 2

    '''
    # variable to store how many items are divisible by divide
    num_divisible = 0 
    
    # loop to iterate through each item in list
    for num in numbers:
        # increment num_visible if there is no remainder
        if num % divide == 0:
                num_divisible += 1
    
    return num_divisible

class ListDivideException(Exception):
    '''Custom Exception Class for a list divide error.'''
    pass

def testListDivide():
    '''Function that contains test scenarios for listDivide function. Error raised if tests fail.'''

    # try to run each test scenario
    try:
        listDivide([1,2,3,4,5])
        listDivide([2,4,6,8,10])
        listDivide([30, 54, 63,98, 100], divide=10)
        listDivide([])
        listDivide([1,2,3,4,5], 1)
    except:
        # raise ListDivideException if there is an error
        raise ListDivideException('Item in one of the lists is not an INT.')


testListDivide()



