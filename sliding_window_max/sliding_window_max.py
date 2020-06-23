'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    '''
    max_value = []
    for n in range(len(num) - k):
        for i in range(k)
            max += num[k]

            if i == k:
                max_value.append(mx)
    '''
    max_value = []
    lst = []
    for n in range(len(nums) - (k - 1)):
        for i in range(k):
            lst.append(nums[i + n])
        max_value.append(max(lst))
        lst.clear()

    return max_value


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
