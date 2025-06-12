import numpy as np

first_array = np.array([2,6,8,4,3,6])
second_array = np.array([[1,2,3,4,5,6],[4,5,6,7,8,9]])

# print("First Array:", first_array)
# print("Second Array:", second_array)

#  to  get the number of dimensions , the .ndim is used
#  use dtype() to get the data type of the array
# use shape() to get the shape of the array
# print(second_array.ndim)

# # indexing in numpy 
# print(second_array[0,4])

# # accessing a specific column
# print(second_array[:,2])

# start index, end index and skipping

# print(first_array[:-1:2])

# # changing an item
# first_array[4] = 9
# print(first_array)


# array initialization
# np.zero() can be used to create a matrix
# np.one() can be used to create a matrix


# print(np.zeros((2,3,2 ))
# )

# np.full_like
# getting random numbers
# np.random.rand(3,2)
# print(np.random.rand(3,2))

# repeating an aray
arr = np.array([[3,4,6,7]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

# difine the number of times of repetition