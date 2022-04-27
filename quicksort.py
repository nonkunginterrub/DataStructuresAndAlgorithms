import sys
from load_number import load_number

numbers = load_number(sys.argv[1])
numbers = numbers.load()

def quicksort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]

    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)

print(numbers)
sorted_number = quicksort(numbers)
print(sorted_number)

# How to run
# python quicksort.py number/8.txt