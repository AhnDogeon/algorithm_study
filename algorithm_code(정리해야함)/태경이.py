import numpy as np
array1 = np.array([[1,1], [1,1], [1,1]]) #x
array2 = np.array([1,1,1]) #v


def hamsoo(array1, array2):
    vv = np.tile(array2, (len(array1[0]), 1))
    print(np.reshape(array1, (len(array1[0]), len(array2))) + vv)
    print(np.reshape(array1, (len(array1[0]), len(array2))) - vv)
    print(np.reshape(array1, (len(array1[0]), len(array2))) * vv)

def isCorrect(array1, array2):
    if len(array1[0]) == len(array2):
        print(True)
        return True
    else:
        print(False)
        return False

z = isCorrect(array1, array2)
if z:
    print(True)
else:
    hamsoo(array1, array2)
    result = isCorrect(array1, array2)