'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    '''
    target = arr.pop(0)
    if target in arr: 
        arr.pop(target) 
    return single_number(target)
    '''
    try:#Try recursive method first
        target = arr.pop(0)
        if target in arr:
            arr.pop(arr.index(target))
        else:
            return target
        return single_number(arr)
    except:#If and exception occurs use a while loop
        while True:
            target = arr.pop(0)
        if target in arr:
            arr.pop(arr.index(target))
        else:
            return target
    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")