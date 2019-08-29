def listDivide (numbers, divide = 2):
    '''Function that takes in a list (numbers) and return how many items are divisible by (divide).
    Arguments:
        numbers (list): Arg for a passed in list.
        divide (int):   Arg for the value used to divide the list items by. Default is 2.
    
    Return:
        num_divisible (int):    The number of elements in list that are divisible by divide.
    '''
    # variable to store how many items are divisible by divide
    num_divisible = 0 
    
    # loop to iterate through each item in list
    for item in numbers:
        # increment num_visible if there is no remainder
        if item % divide == 0:
                num_divisible += 1
    
    return num_divisible

class ListDivideException(Exception):
    pass

def testListDivide():
    '''Function that contains test scenarios for listDivide function

    '''
    listDivide([1,2,3,4,5]) #should return 2
    listDivide([2,4,6,8,10]) #should return 5
    listDivide([30, 54, 63,98, 100], divide=10) # should return 2
    listDivide([]) # should return 0
    listDivide([1,2,3,4,5], 1) # should return 5


testListDivide()



