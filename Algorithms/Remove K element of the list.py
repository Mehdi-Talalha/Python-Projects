import copy

def remove_and_sort(Lin, k):
    """ Lin is a list of ints
        k is an int >= 0
    Mutates Lin to remove the first k elements in Lin and 
    then sorts the remaining elements in ascending order.
    If you run out of items to remove, Lin is mutated to an empty list.
    Does not return anything.
    """
    # Your code here  
    if k < len(Lin):
        # copy the original list to iterate over it (remove method issue!)
        Nlin = copy.copy(Lin)
        for i in range(len(Nlin)):
            if i < k:
                Lin.remove(Lin[i])

# Examples:
L = [1,6,3]
k = 6
remove_and_sort(L, k)
print(L)   # prints the list [3, 6]