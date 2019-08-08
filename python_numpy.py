# -*- coding: utf-8 -*-
"""
Created on Tue May 22 09:47:09 2018

@author: Maximo_Lai
"""

#Arrays basic
import numpy as np

a = np.array([1, 2, 3])            # Create a rank 1 array
b = np.array([[1,2,3],[4,5,6]])    # Create a rank 2 array
print(type(a))            # Prints "<class 'numpy.ndarray'>"
print(a.shape)            # Prints "(3,)" array size is 1 x 3
print(b.shape)            # Prints "(2, 3)" array size is 2 x 3

#Create an array of series number
a = np.arange(4)      # "[0,1,2,3]"
# Create an array of all zeros
a = np.zeros((2,2))   # "[[ 0.  0.]
                      #  [ 0.  0.]]"
# Create an array of all ones
b = np.ones((1,2))    # "[[ 1.  1.]]"
# Create a constant array
c = np.full((2,2), 7) # "[[ 7.  7.]
                      #  [ 7.  7.]]"
# Create a 2x2 identity matrix
d = np.eye(2)         # "[[ 1.  0.]
                      #  [ 0.  1.]]"
# Create an array filled with random values
e = np.random.random((2,2))  
                      # "[[ 0.91940167  0.08143941]
                      #  [ 0.68744134  0.87236687]]"       
                      
#Array indexing by Slicing
a = np.array([[1,2,3,4],\
              [5,6,7,8],\
              [9,10,11,12]])
b = a[1, :]    # Get values of the second row of a
# Use slicing to pull out the subarray consisting of the first 2 rows
# and columns 1 and 2; b is the following array of shape (2, 2):
# [[2 3]
#  [6 7]]
b = a[:2, 1:3]
# A slice of an array is a view into the same data, so modifying it
# will modify the original array.
a[:2, 1:3] = 0
print(a)
# [[ 1,  0,  0,  4],
#  [ 5,  0,  0,  8],
#  [ 9, 10, 11, 12]]

#Array indexing by Integer array indexing
# Create a new array from which we will select elements
a = np.array([[1,2,3],\
              [4,5,6],\
              [7,8,9],\
              [10, 11, 12]])
# Create an array of indices
b = np.array([0, 2, 0, 1])
# Select one element from each row of a using the indices in b
print(a[np.arange(4), b])  # Prints "[ 1  6  7 11]"

#Array indexing by Boolean array indexing
a = np.array([[1,2],\
              [3, 4],\
              [5, 6]])

bool_idx = (a > 2)   # Find the elements of a that are bigger than 2;
                     # this returns a numpy array of Booleans of the same
                     # shape as a, where each slot of bool_idx tells
                     # whether that element of a is > 2.

print(bool_idx)      # Prints "[[False False]
                     #          [ True  True]
                     #          [ True  True]]"

# We use boolean array indexing to construct a rank 1 array
# consisting of the elements of a corresponding to the True values
# of bool_idx
print(a[bool_idx])  # Prints "[3 4 5 6]"

# We can do all of the above in a single concise statement:
print(a[a > 2])     # Prints "[3 4 5 6]"