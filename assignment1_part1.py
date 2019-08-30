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
    # try to run each test scenario and raise error is item in list can't be divided
    try:
        a_test = listDivide([1,2,3,4,5])
        b_test = listDivide([2,4,6,8,10])
        c_test = listDivide([30,54,63,98,100], divide=10)
        d_test = listDivide([])
        e_test = listDivide([1,2,3,4,5], 1)
    except:
        # raise ListDivideException if there is an error
        raise ListDivideException('There is a non divisible value in one of the lists!')

    # check that each test list has the correct return values
    if a_test == 2 and b_test == 5 and c_test == 2 and d_test == 0 and e_test == 5:
        pass
    else:
        raise ListDivideException('There is a return value problem with the tests.')    
  

testListDivide()



