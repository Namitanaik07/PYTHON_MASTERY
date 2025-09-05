import numpy as np #import numpy as np  # Ensure NumPy is installed
#python.exe -m pip install --upgrade pip
arr=np.array([1,2,3,4,5])#from list to array

zeros=np.zeros((3,3))#3x3 matrix of zeros
ones=np.ones((2,4))#2x4 matrix of ones
import numpy as np  

arr = np.array([1, 2, 3, 4, 5])   # from list to array  
zeros = np.zeros((3, 3))          # 3x3 matrix of zeros  
ones = np.ones((2, 4))            # 2x4 matrix of ones  
reshape_arr = arr.reshape((5, 1))  # Reshape to 5x1 matrix
print("Array:", arr)  
print("Zeros:\n", zeros)  
print("Ones:\n", ones)  
print("Reshaped Array:\n", reshape_arr)

random_array=np.random.rand(3,3)#3x3 matrix of random numbers
print("Random Array:\n", random_array)
random_integers=np.random.randint(1,10,size=(3,3))#3x3 matrix of random integers between 1 and 10
print("Random Integers:\n", random_integers)
