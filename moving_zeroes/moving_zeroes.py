'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    '''
    Move non zero integers to left order not important
    loop through the len(arr)
    pop and append all zeros to the end of the list
    return the mutated list
    '''
    #Original solution does not pass final test but otherwise is a valid solution
    for idx in range(len(arr)):
        #originally is 0
        if arr[idx] != 0:
            #originally .append(arr.pop(idx))
            arr.insert(0, arr.pop(idx))

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")