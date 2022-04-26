def recursive_binary_search(list, traget):
    if len(list) == 0:
        return False
    else:
        midpoint = (len(list))//2

        if list[midpoint] == traget:
            return True
        elif list[midpoint] < traget:
            return recursive_binary_search(list[midpoint+1:], traget)
        else:
            return recursive_binary_search(list[:midpoint], traget)
    
def verify(result):
    print("Traget found: ", result)

numbers = [1,2,3,4,5,6,7,8,9,10]

result = recursive_binary_search(numbers, 12)
verify(result)

result = recursive_binary_search(numbers, 6)
verify(result)