'''
a ** b 
형태에서 ** 연산자는 거듭제곱(지수 연산)을 수행하는데 사용된다.

a^b 와 같다.

**연산자의 특징은 정수, 실수 모두 적용이 가능하다.

'''

from PySide2.QtGui import QMatrix4x4, QVector3D
import math

print()
matrix1 = QMatrix4x4(
    0.0523866, 0.282124, -0.957947, 39.788, 
    -0.62508, 0.757366, 0.188867, -371.121, 
    0.778801, 0.5889, 0.216026, -149.512, 
    0, 0, 0, 1
)

matrix2 = QMatrix4x4(
    0.0523866, 0.282124, -0.957947, 38.9296, 
    -0.62508, 0.757366, 0.188867, -390.446, 
    0.778801, 0.5889, 0.216026, -161.477, 
    0, 0, 0, 1
)

pos1 = QVector3D(matrix1[0, 3], matrix1[1, 3], matrix1[2, 3])
pos2 = QVector3D(matrix2[0, 3], matrix2[1, 3], matrix2[2, 3])

distance = math.sqrt(
    (pos1.x() - pos2.x())**2 + 
    (pos1.y() - pos2.y())**2 + 
    (pos1.z() - pos2.z())**2
)

print(distance)