import numpy as np

# **int8:** 8-bit signed integer (-128 to 127).
#
# **int16:** 16-bit signed integer (-32,768 to 32,767).
#
# **int32:** 32-bit signed integer (-2,147,483,648 to 2,147,483,647).
#
# **int64:** 64-bit signed integer (-9,223,372,036,854,775,808 to 9,223,372,036,854,775,807).
#
# **uint8:** 8-bit unsigned integer (0 to 255).
#
# **uint16:** 16-bit unsigned integer (0 to 65,535).
#
# **uint32:** 32-bit unsigned integer (0 to 4,294,967,295).
#
# **uint64:** 64-bit unsigned integer (0 to 18,446,744,073,709,551,615).
#
# **float16:** 16-bit floating point.
#
# **float32:** 32-bit floating point.
#
# **float64:** 64-bit floating point (double precision).
#
# **complex64:** Complex number with 32-bit real and imaginary parts.
#
# **complex128:** Complex number with 64-bit real and imaginary parts.
#
# **bool:** Boolean type (True or False).
#
# **str:** String (sequence of characters).
#
# `dtype` data type of an array. `astype` is used to convers NumPy array into exact data type

import numpy as np
arr1 = np.array([1, 2, 3]) # simple array
print(arr1.dtype)

arr1 = np.array(arr1, dtype = np.float64)
print(arr1)
print(arr1.dtype)

float_arr1 = arr1.astype(np.float32)
print(float_arr1.dtype)

array = np.array([1.3, 5.3,  1.8, 10.3])
print(array)
print(array.dtype)

int_array = array.astype(np.int64)
print(int_array)

print(int_array.dtype)

# Practice

### Task 1: Shape and Size

# You have a NumPy array with unknown dimensions. Write a function that takes any NumPy array and returns its shape and size.


import numpy as np
array = np.random.randint(0, 100, size=21)
print(array.size)
print(array.shape)

# Task 2: Zeros and Ones

# Create a function that generates a square matrix (size n x n) filled with ones on the border and zeros inside.

import numpy as np
def matrix1(n):
  mat1 = np.zeros((n, n))
  return mat1
matrix1(4)
print(matrix1(4))

#---------------------------
# getting dimensions from a user

def matrix2(n):
  mat2 = np.ones(shape=(n, n))
  return mat2
n = int(input("Enter a dimension of the matrix\n>>>"))
matrix2(n)

#Task 3: Arange

# Write a function that creates an array of even numbers between 10 and 100 with a step of 5.
#
# First code is writen as its working with python list.(normal operation)
#
# Second code is writen using numpy operation: do not require loops.(vectorized operation)
# """

# first version
import numpy as np
def even(s, e, p):
  even_arr = []
  arr = np.arange(s, e, p)
  i = 0
  while i < len(arr):
    if arr[i] % 2 == 0:
      even_arr.append(arr[i])
      array = np.array(even_arr)
    i+=1
  return array
print(even(10, 101, 5))

# second version
import numpy as np
def even(s, e, p):
  arr = np.arange(s, e, p)
  even_array = arr[arr % 2 == 0]
  return even_array
print(even(10, 101, 5))

# Task 4: Astype and Dtype

# Given a NumPy array of integers, write a function that converts it to a float type and verifies the type change.


import numpy as np
int_ar = np.array([1, 2, 3, 4, 5, 6, 6])
print(int_ar.dtype)

fl_ar = int_ar.astype(float)
print(fl_ar.dtype)

import numpy as np
def data_change(arr):
  float_array = arr.astype(float)
  verified = float_array.dtype == np.float64
  return f"{float_array}\nArrays type is: {float_array.dtype}\n{verified}"

arr = np.array([1, 2, 3, 4, 5, 6, 6])
print(data_change(arr))