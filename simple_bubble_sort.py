def binary_search(lst, number_to_find):
    left_index = 0
    right_index = len(lst)-1
    
    mid_index = 0   # for comparison with number_to_find
    #logic
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = lst[mid_index]
        #compare this value with number_to_find
        if mid_number == number_to_find:
            return mid_index
        
        if mid_number < number_to_find:   # mid value is lesser than number_to_find
            left_index = mid_index + 1
        
        else:   # mid value lesser than middle value
            right_index = mid_index - 1
    
    return -1

lst = [0,1,2,3,4,5,6,7]
number_to_find = 2

print(binary_search(lst, number_to_find)) #2
