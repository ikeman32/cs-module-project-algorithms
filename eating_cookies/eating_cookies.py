'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
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

    if cache is None:
        cache = {}

    if n in cache:
        return cache[n]
    
        
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
