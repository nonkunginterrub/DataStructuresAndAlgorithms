
def linear_search(list, traget):
    """
    Return the index position of the target if found, else returns None
    """
    for i in range(0, len(list)):
        if list[i] == traget:
            return i
        
    return None

def verify(index):
    if index is not None:
        print("Traget found at index: ", index)
    else:
        print("Traget not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(numbers, 12)
verify(result)

result = linear_search(numbers, 6)
verify(result)