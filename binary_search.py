def binary_search(list, traget):
    first = 0
    last = len(list) - 1
    
    while first <= last:
        midpoint = (first + last)//2
        
        if list[midpoint] == traget:
            return midpoint
        elif list[midpoint] < traget:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None

def verify(index):
    if index is not None:
        print("Traget found at index: ", index)
    else:
        print("Traget not found in list.")

numbers = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(numbers, 12)
verify(result)

result = binary_search(numbers, 5)
verify(result)