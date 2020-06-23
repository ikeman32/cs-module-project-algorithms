'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    '''
    Multiply all number in list except number at index
    insert produce at index
    need outer and inner loop
    pop number at outer idx
    in inner loop multiply by idx
    inner loop len(arr)
    at outer loop insert product at inner idx
    '''
    keep = []
    for o_idx in range(0, len(arr)):
        product = 1
        tmp = arr.pop(o_idx)
        

        for i_idx in range(len(arr)):
            product *= arr[i_idx]
        
        keep.append(product)
        arr.insert(o_idx, tmp)

    return keep


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
