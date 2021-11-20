
def selection_sort(values):
    sorted_list=[]
    print('%-25s %-25s' % (values, sorted_list))

    for i in range(0,len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        print('%-25s %-25s' % (values, sorted_list))

    return sorted_list

def index_of_min(values):
    min_index=0
    for i in range(1,len(values)):
        if values[i]<values[min_index]:
            min_index=i
    return min_index

numbers=[5,8,4,7,1,4,8,9,2]

print(selection_sort(numbers))#Returns sorted list

#not fast enough



# # Let's implement the function that will do our selection sort.
# # We're going to pass in our Python list containing all the unsorted
# # numbers.
# def selection_sort(values):
#   # We'll create an empty list that will hold all our sorted values.
#   sorted_list = []
#   # We'll loop once for each value in the list.
#   for i in range(0, len(values)):
#     # We call a function named index_of_min, which we're going to
#     # write in just a minute, that find the minimum value in the
#     # unsorted list and return its index.
#     index_to_move = index_of_min(values)
#     # Then we call the "pop" method on the list, and pass it the
#     # index of the minimum value. pop will remove that item from the
#     # list and return it. We then add that value at the end of the
#     # sorted list.
#     sorted_list.append(values.pop(index_to_move))
#   # Going up a level of indentation signals to Python that we're
#   # ending the loop. After the loop finishes, we return the sorted
#   # list.
#   return sorted_list

# # Now we need to write the function that picks out the minimum value.
# # We pass in the list we're going to search.
# def index_of_min(values):
#   # We mark the first value in the list as the minimum. It may or may
#   # not be the actual minimum, but it's the smallest we've seen on
#   # this pass through the list. (It's also the only value we've seen
#   # on this pass through the list so far.)
#   min_index = 0
#   # Now we loop through the remaining values in the list after the
#   # first.
#   for i in range(1, len(values)):
#     # We test whether the value we're currently looking at is less
#     # than the previously recorded minimum.
#     if values[i] < values[min_index]:
#       # If it is, then we set the current index as the new index of
#       # the minimum value.
#       min_index = i
#   # After we've looped through all the values, we return the index of
#   # the smallest value we found.
#   return min_index

# # Lastly, we need to actually run our selection sort method, and
# # print the sorted list it returns.
# print(selection_sort(numbers))