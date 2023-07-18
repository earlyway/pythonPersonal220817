import math
clearFindCache()

LHand =  vrDeviceService.getLeftTrackedHand()

ff = LHand.getJointTransform(vrHandTypes.Thumb,2)
fff = LHand.getJointTransform(vrHandTypes.Thumb,4)
gg = LHand.getJointTransform(vrHandTypes.Index,3)
g = LHand.getJointTransform(vrHandTypes.Index,4)
hh = LHand.getJointTransform(vrHandTypes.Middle,3)
h = LHand.getJointTransform(vrHandTypes.Middle,4)
i = LHand.getTransform()


print("index3 QMatrix " + str(gg))
print("index4 QMatrix " + str(g))
print("middle3 QMatrix " + str(hh))
print("middle4 QMatrix " + str(h))
print("left VHand position QMatrix " + str(i))


convertT = vrMathService.getTranslation(ff)
convertII = vrMathService.getTranslation(gg)
convertI = vrMathService.getTranslation(g)
convertMM = vrMathService.getTranslation(hh)
convertM = vrMathService.getTranslation(h)
convertHand = vrMathService.getTranslation(i)


print("convert Index3 = " + str(convertII))
print("convert Index4 = " + str(convertI))
print("convert Middle3 = " + str(convertMM))
print("convert Middle4 = " + str(convertM))
print("convertHand  = " + str(convertHand))

''' # world 좌표 = 상대좌표 Matrix
perspective = vrNodeService.findNode("Perspective")
camPos = perspective.getWorldTransform()

#invCamPos = camPos.inverted()[0]

#yUpMatrix = QMatrix4x4(1,0,0,0,0,0,-1,0,0,1,0,0,0,0,0,1)

#world = i / invCamPos / yUpMatrix
#print("worldHandPos" + str(world))

world = vrMathService.getTranslation(camPos * i)
print("worldHandPos " + str(world))

ww = camPos * i
print("camPos * i " + str(ww))

wk = vrNodeService.findNode("cubeOrange")
fuu = vrdNode.getWorldTransform(wk)

print("fuu " + str(fuu))

'''

pos1 = QVector3D(g[0,3], g[1,3], g[2,3])
pos2 = QVector3D(fff[0,3], fff[1,3], fff[2,3])

distance1 = math.sqrt(
    (pos1.x() - pos2.x())**2 +
    (pos1.y() - pos2.y())**2 +
    (pos1.z() - pos2.z())**2
    )
    
print("distance1 " + str(distance1))


pos3 = QVector3D(i[0,3], i[1,3], i[2,3])
pos4 = QVector3D(fuu[0,3], fuu[1,3], fuu[2,3])

distance2 = math.sqrt(
    (pos3.x() - pos4.x())**2 +
    (pos3.y() - pos4.y())**2 +
    (pos3.z() - pos4.z())**2
    )
print("distance2 " + str(distance2))


yu = vrNodeService.findNode("Box2")
oee = vrdNode.getWorldTransform(yu)
matrix1 = QMatrix4x4(
    0.0523866, 0.282124, -0.957947, 39.788, 
    -0.62508, 0.757366, 0.188867, -371.121, 
    0.778801, 0.5889, 0.216026, 149.512, 
    0, 0, 0, 1
)


pos5 = QVector3D(oee[0, 3], oee[1, 3], oee[2, 3])

distance3 = math.sqrt(
    (pos5.x() - pos4.x())**2 + 
    (pos5.y() - pos4.y())**2 + 
    (pos5.z() - pos4.z())**2
)
print(distance3)



