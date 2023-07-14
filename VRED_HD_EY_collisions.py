
moving = findNode("8")
target = findNode("pinkBox")
target2 = findNode("purpleBox")
movingTumbler = findNode("moving_Tumbler1")
#updateScene()

def targetWorldPos():
    moving.setWorldTranslation.z(726) #pinkBox set
    print("pinkBox set")

def targetWorldRot():
    moving.setRotation(0,0,0)

def target2WorldPos():
    moving.setWorldTranslation.z(726) #purpleBox set
    
    print("purpleBox set")

def target2WorldRot():
    moving.setRotation(0,0,0)
    
def target3WorldRot():
    movingTumbler.setRotation(0,0,0)
    po = movingTumbler.getWorldTranslation()
    print("x pos" + str(po[1]))
    movingTumbler.setWorldTranslation(po[0], po[1], float(726.0))


collVar = vrCollision([moving],[target])
collVar.connect(targetWorldPos)
collVar.connect(targetWorldRot)


collVar2 = vrCollision([moving],[target2])
collVar2.connect(target2WorldPos)
collVar2.connect(target2WorldRot)



collVar3 = vrCollision([movingTumbler],[target2])
collVar3.connect(target3WorldRot)
