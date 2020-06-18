'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):
    '''
    eat n cookies x ways
    were a cookies can be eaten at one time
    if n == 0:
        return 1
    
    if n < 0:
        return 0
        
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)
    '''
    if n == 0:
        return 1
    
    if n < 0:
        return 0
        
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 0

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
