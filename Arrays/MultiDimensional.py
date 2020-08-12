############################### MultiDimensional Arrays #######################

# Declaration of Multi-Dimensional Arrays
# n x m 
arr = [ 
       [3, 5, 10], 
       [11, 12, 13], 
       [14, 1, 0],
       [11, 4, 2]
]

# print(len(arr))

# Element at 2 row and 3 column
# print(arr[1][2])

# Getting all elements of the multi dimensional Array using for loop

for outerIndex in range(0, len(arr)):
    for innerIndex in range(0, len(arr[outerIndex])):
        print(arr[outerIndex][innerIndex])
    print()