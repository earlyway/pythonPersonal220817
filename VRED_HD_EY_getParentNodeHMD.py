
clearFindCache()

we = findNode("Perspective")
a = vrNodeService.findNode("Perspective")

b = vrdNode.getParent(a)
asasa = b.getName
vlf = b.getWorldTransform()


print("Perspective 노드의 상위 노드 getParent " + str(b)) # Perspective 노드의 상위 노드
print("Perspective 노드의 상위 노드의 이름 " + str(asasa))
print("vlf" + str(vlf))

d = vrdTransformNode.getTranslation(a)
print("Perspective 노드의 상대좌표 get local Translation " + str(d)) #Perspective 노드의 상대좌표 Vector3



c = vrdNode.getWorldTransform(a) # Perspective 노드의 상위 노드의 월드 좌표
print("Perspective 노드의 월드 좌표 get World Transform " + str(c)) #Perspective 노드의 월드 좌표 QMatrix4x4

e = vrdGeometryNode.getWorldTranslation(a)
#e = vrdGeometryNode.getWorldTranslation(b) #상위 노드의 월드좌표를 가지고오고 싶었지만 리턴타입때문에 불가능
print("Perspective 노드의 get World Translation" + str(e))

#f = vrdGeometryNode.getPositions(b)
f = vrdGeometryNode.getTranslation(a)
print("Perspective 노드의 get local Translation" + str(f))




LHand =  vrDeviceService.getLeftTrackedHand()

ff = LHand.getJointTransform(vrHandTypes.Thumb,2)
fff = LHand.getJointTransform(vrHandTypes.Thumb,4)
gg = LHand.getJointTransform(vrHandTypes.Index,3)
g = LHand.getJointTransform(vrHandTypes.Index,4)
hh = LHand.getJointTransform(vrHandTypes.Middle,3)
h = LHand.getJointTransform(vrHandTypes.Middle,4)
i = LHand.getTransform()



left = vrDeviceService.getVRDevice("left-controller")  #return : vrdVRDevice

dwq = vrNodeService.findNode("left-controller")
eed = vrdNode.getParent(dwq)
aad = vrdNode.getWorldTransform(dwq)
#ekj = vrdTransformNode.getTranslation(dwq)
tr = vrdNode.getName(dwq)
ry = vrdNode.getName(eed)
ro = vrdNode.getChildCount(dwq)
ao = vrdNode.getChildren(dwq)
io = left.getNode()
ii = left.getName()
ik = left.getTrackingMatrix()
ib = vrdNode.getChildren(io)
iv = vrdNode.getParent(io)
ic = iv.getName()


print("left hand의 상위 노드 " + str(eed))
print("left hand의 translation " + str(dwq))
print("left hand의 절대 좌표 " + str(aad))
print("left hand의 getName " + str(tr))
print("left hand의 상위 노드의 getName " + str(ry))
print("left hand의 하위 노드 갯수 " + str(ro))
print("left hand의 하위 노드 " + str(ao))
print("left hand의 노드 " + str(io))
print("left hand 의 이름 " + str(ii))
print("left hand의 matrix " + str(ik))
print("left hand의 하위 노드 " + str(ib))
print("left hand의 상위 노드 " + str(iv))
print("left hand의 상위 노드의 이름 " + str(ic))




#yr = vrdSessionUser.getLeftHandNode
#print(yr)
#rryy = vrdNode.getName(yr)
#print rryy
#vrdSessionUser.getLeftHandTrackingMatrix
#vrdSessionUser.getCameraMatrix



#ds = vrdNode.getChildCount(i)
#print(ds)

#bg = fff.getTranslation
#print(bg)
print(str(Finger_Thumb))
print(str(Finger_Index))
print(str(Finger_Middle))
print(str(Finger_Ring))
print(str(Finger_Pinky))



