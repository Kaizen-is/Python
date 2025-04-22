import numpy as np
def nd_array():
  arr = np.arange(0, 9).reshape(3, 3)
  return arr
print(nd_array())


arr = nd_array()
assert arr.size == 9,
assert type(arr) == np.ndarray,y
# elementwise test
test_arr = np.arange(9).reshape(3, 3)
assert arr.shape == (3, 3), 
assert True in np.in1d(arr, test_arr), 


def sliced_array_2d():
  
    array = nd_array()
    return array[2, 0:2]
print(sliced_array_2d())


sl_arr_2d = sliced_array_2d() 
assert sl_arr_2d.size == 2,
assert type(sl_arr_2d) == np.ndarray, 
test_arr = np.array([6, 7])
assert sl_arr_2d.shape == (2,), 
assert True in np.in1d(sl_arr_2d, test_arr)
