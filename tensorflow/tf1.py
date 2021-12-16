import tensorflow as tf
import numpy as np

matrix1 = np.array([(1,2,3),(5,6,7),(9,10,11)],dtype='int32')
matrix2 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype='int32')

print(matrix1)
matrix1_prod = tf.matmul(matrix1, matrix2)
print(matrix1_prod)