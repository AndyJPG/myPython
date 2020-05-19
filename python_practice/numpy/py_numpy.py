import numpy as np
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
arr_5d = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print(arr_3d)
print(arr_5d)
print(np.__version__)
print(type(arr))

print(arr[0])
print('2nd element on 1st dim: ', arr_2d[0, 1])
print('3nd element on 2st dim on 1st dim', arr_3d[0, 1, 2])

print(arr[1:5])
print(arr[::2])
print(arr_2d[0, 1::2])
print(arr_2d[0:2, 1])

print(arr.dtype)

arr_with_dtype = np.array([1, 2, 3, 4], dtype='S')
arr_float = np.array([1.2, 4.5, 2.1])

print(arr_with_dtype.dtype)
print(arr_float.astype('i'))

# copy & view

arr_view = arr.view()
arr_copy = arr.copy()

print('a change in original array will reflect on x vice versa ', arr_view)
print('Copy owns the data: ', arr_copy.base)
print('View doesn\'t own the data: ', arr_view.base)

# shape
print('arr_2d has 2 dimensions and 3 elements in each dimension ', arr_2d.shape)
print('shape of array : ', arr_5d.shape)

print(arr.reshape(4, 3))
print('1 dimension to 3 dimensions : ', arr.reshape(2, 3, 2))
print(arr.reshape(4, 3).base)
print('No specify exact umber pass -1 for numpy to auto calculate : ', arr.reshape(2, 2, -1))
print('Flat array : ', arr_3d.reshape(-1))

# iterate with nditer
for x in np.nditer(arr_3d):
    print(x)

# buffer
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

for x in np.nditer(arr_2d[:, ::2]):
    print(x)

for idx, x in np.ndenumerate(arr_3d):
    print(idx, x)

print(np.concatenate((arr, arr), axis=0))
print(np.concatenate((arr_2d, arr_2d), axis=1))

print(np.stack((arr, arr), axis=0))
print(np.hstack((arr_2d, arr_2d)))
print(np.vstack((arr, arr)))
print(np.dstack((arr, arr)))

# splitting
print(np.array_split(arr, 3))
print(np.array_split(arr_2d, 3))
print(np.array_split(arr_2d, 2, axis=1))

# search
print('Search value and return the index : ', np.where(arr == 4))
print('Search even number : ', np.where(arr%2 == 0))

# binary search with searchsorted
print(np.searchsorted(arr, 7))

np.sort(arr)

# filter
arr2 = np.array([2, 3, 4, 5, 19, 90])
x = [True, False, True, False, False, False]
loop_x = []

for element in arr2:
    if element > 2:
        loop_x.append(True)
    else:
        loop_x.append(False)

print(arr2[x])
print(arr2[loop_x])

filter_arr = arr2 % 2 == 1
print(arr2[filter_arr])

# Random number
print(random.randint(100))
print(random.rand())
print(random.randint(100, size=(10)))
print(random.choice(arr))


# Matplotib
nor_dist = random.normal(loc=50, scale=5, size=1000)
sns.distplot(nor_dist, hist=False, label='normal')

bio_dist = random.binomial(n=100, p=0.5, size=1000)
sns.distplot(bio_dist, hist=False, label='binomial')

plt.show()
