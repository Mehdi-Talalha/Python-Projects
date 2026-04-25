# i tried to make max (built in function)

def is_value(x):
    # this function check if the item is a single value or (list, tuple) and turn everythings to single values
    if isinstance(x, (list, tuple)):
        if not x:
            # return the lowest value possible
            return float('-inf')
        # unpack the list or the tuple
        return max(*x)
    else:
        return x
    
def max(*items):
    # make sure it not empty
    if not items:
        return "EmptyTuple"

    # set the first item as highest one
    HIGH = is_value(items[0])

    # main for loop
    for i in items:
        
        i = is_value(i)

        # cause we cannot compare values with defferent types
        if type(i) != type(HIGH):
            raise TypeError("cannot compare str and int")

        if i > HIGH:
            HIGH = i
            
    return HIGH


result = max(5,[5, 55],5)
print("the highest item is {}".format(result)) 