from array import array

import numpy as np
arr_1 = np.array([1,2,4])
print(arr_1)

zero_array = np.zeros((4,5))
print(zero_array)

range_array = np.arange(1,11,2)
print(range_array)

random_array = np.random.rand(4,5)
print(random_array)

# Shape defines the number of rows and columns
# Size defines the number of objects

print(zero_array.shape)
print(zero_array.size)

print(zero_array.ndim)

print(zero_array.dtype)

# Array indexing and slicing

print(range_array[1])

arr_2 = np.array(([1,2,4], [1,2,2]))
print(arr_2[1,2])
print("Next")
subarray =  arr_2[0:3,1]
print(subarray)

print(arr_2[arr_2 > 2])

# broadcasting

print(arr_1 + arr_2)
print("Next")
print("  ")
## Mathematical Operations

# Element wise operation

print (arr_2 * 12)

# Aggregate functions

print(np.sum(arr_2))
print(np.mean(arr_2))
print(np.std(arr_2))

print("Next")
print("  ")

## Linear Algebra

# Dot product

A = np.array([1,2,3,4])
B = np.array([2,3,4,5])
print(np.dot(A, B))

# Eigen values and vectors
z = np.array([[1, 2], [3, 4]])
eigenvalues = np.linalg.eig(z)
print(eigenvalues)

# Summation along axes

print(np.sum(z, axis=0))
print(np.sum(z, axis=1))

print("Next")
print(" Functions ")
# Functions and iteration

def add_arrays(array1, array2):
    return np.add(array1, array2)

print(add_arrays(A,B))

def filter_greater_than(array, threshold):
    return array[array > threshold]

print((filter_greater_than(A, 1)))

def calculate_stats(array):
    return {
        "mean": np.mean(array),      # Average
        "sum": np.sum(array),        # Total sum
        "std_dev": np.std(array)     # Standard deviation
    }

a = np.array([10, 20, 30, 40, 50])
print(calculate_stats(a))

## Iteration
print("Iteration")
print("----------------")

abc = np.zeros_like(a)

for i in range(len(a)):
    if i == 0:
        abc[i] = a[i]
    else:
        abc[i] = a[i] - a[i-1]

print(abc)

d = np.array([2,4,6,7,9])
e = np.array([2,4,6,5,4])
f = np.zeros_like(d)
def sumofarrays(a,b):
    f = np.zeros_like(a)
    for i in range(len(a)):
        f[i] = a[i] + b[i]
    print(f)
print("sum:")
print(sumofarrays(d,e))

def double_odd_rows(matrix):
    for rows in mat:
        for element in rows:  # Iterate over row indices
            if rows() % 2 == 1:  # Check if row index is odd
                matrix[i] *= 2
        return matrix

mat = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(double_odd_rows(mat))




