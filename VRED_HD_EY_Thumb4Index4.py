import math

LHand =  vrDeviceService.getLeftTrackedHand()


t4 = LHand.getJointTransform(vrHandTypes.Thumb,4) #thumb joint4 의 QMatrix4x4
i4 = LHand.getJointTransform(vrHandTypes.Index,4)

print("t4 " + str(t4))
print("i4 " + str(i4))

vbvb= vrMathService.getTranslation(t4)
vsvs = vrMathService.getTranslation(i4)
print(str(vbvb))
print(str(vsvs))

t4Vect3 = QVector3D(t4[0,3], t4[1,3], t4[2,3])
i4Vect3 = QVector3D(i4[0,3], i4[1,3], i4[2,3])

distance_t_i = math.sqrt(
    (t4Vect3.x() - i4Vect3.x())**2 +
    (t4Vect3.y() - i4Vect3.y())**2 +
    (t4Vect3.z() - i4Vect3.z())**2
)

print("Thumb4 between index4 " + str(distance_t_i))



'''
g = LHand.getJointTransform(vrHandTypes.Index,4)
fff = LHand.getJointTransform(vrHandTypes.Thumb,3)

pos1 = QVector3D(g[0,3], g[1,3], g[2,3])
pos2 = QVector3D(fff[0,3], fff[1,3], fff[2,3])

distance1 = math.sqrt(
    (pos1.x() - pos2.x())**2 +
    (pos1.y() - pos2.y())**2 +
    (pos1.z() - pos2.z())**2
    )
    
print("distance1 " + str(distance1))
'''





