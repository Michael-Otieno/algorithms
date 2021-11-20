def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list and divides into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step
    """
    if len(list)<=1:##stopping condition
        return list

    left_half, right_half=split(list)
    left=merge_sort(left_half)
    right=merge_sort(right_half)

    return merge(left,right)

def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    Takes overall 0(log n)
    """
    mid = len(list)//2
    left = list[:mid]#from start to middle of list
    right = list[mid:]#from start from beginning

    return left,right

def merge(left,right):
    """
    Merges two lists(array),sorting them in the process
    Returns a new merged list


    Runs in overall 0(n log n) time
    """
    l=[]#new list to be returned
    i=0#keep track of indexes in the left list 
    j=0#keep track of indexes in the right list

    while i<len(left) and j<len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i+=1
        else:
            l.append(right[j])
            j+=1
    while i<len(left):
        l.append(left[i])
        i+=1

    while j<len(right):
        l.append(right[j])
        j+=1 
    return l

# alist=[45,32,45,66,78,22,1,33,9,6]
# l=merge_sort(alist)
# print(l)
def verify_sorted(list):
    n=len(list)

    if n==0 or n==1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])
    
alist=[45,32,45,66,78,22,1,33,9,6]
l=merge_sort(alist)
print(verify_sorted(alist))
print(verify_sorted(l))  