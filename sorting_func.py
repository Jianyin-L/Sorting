# This file can be used to sort a list of number without using the sort function
# Intuition： 
# 1. find the minimum element of the unsorted list
# 2. Add it to the sorted list. 
# 3. Remove it from the unsorted list. 
# 4. Continue to do so until the unsorted list is exhausted. 


def sorting(unsorted):
    
    '''
    unsorted: the unsorted list
    '''

    # Define a list to store sorted element
    sorted = []

    # Obtain the length of the unsorted list
    unsorted_len = len(unsorted)

    # The process will stop when the length of the sorted list is the same the length of the unsorted list. 
    while len(sorted) != unsorted_len:
        
        # Find the smallest element
        minimum = min(unsorted)

        # Add it to the sorted list
        sorted.append(minimum)

        # Remove the element from the unsorted list
        unsorted.remove(minimum)

    # Return the result
    return sorted


a_list = [5,4,3,2,1]
# a_list = [5,5,4,4,3,3]    # Works with duplicate number
# a_list = [-1, -0.99, -0.0009, 100]    # Works with negative number

result = sorting(a_list)
print(result)