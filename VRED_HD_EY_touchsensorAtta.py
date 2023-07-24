def createTouchSensorTumb(node):
    # Create the touch sensor first. This will create the needed
    # attachment and register the touch sensor in VRED_MSG_PROJECT_MERGED
    touchSensor = vrTouchSensor(node)
    
    # To add a variant set, that will be called whenever the touch
    # sensor is activated, we need to modify the attachement and
    # add the variant set directly.
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)
    
    # Note: this takes a list as parameter, so you can trigger multiple
    # variant sets
    touchSensorAttAccess.setMString("variantSets", ["toggleColor"])
    print("Attach tumbler touchsensor")

    return touchSensor
    
'''
def createTouchSensor1(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)
    
    touchSensorAttAccess.setMString("variantSets", ["1touchsensor"])

    return touchSensor
'''
def createTouchSensor2(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["2constraint"])
    print("Attach number2 touchsensor")

    return touchSensor
    
def createTouchSensor3(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["3collisionPrint"])
    print("Attach number3 touchsensor")

    return touchSensor
    
def createTouchSensor4(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["num4Const"])
    print("Attach number4 touchsensor")

    return touchSensor
    
def createTouchSensor5(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["num5Const"])
    print("Attach number5 touchsensor")

    return touchSensor
    
def createTouchSensor6(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["num6Const"])
    print("Attach number6 touchsensor")

    return touchSensor
    
def createTouchSensor8(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["getPinchStr8"])
    print("Attach number8 touchsensor")

    return touchSensor
    
def createTouchSensorMov_Tumb(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["getPinchStrTumb"])
    print("Attach moving_Tumb touchsensor")

    return touchSensor
    
def createTouchSensorMov_thu_ind(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["finger_t_i_FollowCubeLoop"])
    print("Attach finger_t_i_FollowCubeLoop touchsensor")

    return touchSensor
    
def createTouchSensorDeact(node):
    touchSensor = vrTouchSensor(node)
    touchSensorAtt = node.getAttachment("TouchSensorAttachment")
    touchSensorAttAccess = vrFieldAccess(touchSensorAtt)

    touchSensorAttAccess.setMString("variantSets", ["ConstDeactive"])
    print("Attach ConstDeactive touchsensor")

    return touchSensor


tsensorTumbler = createTouchSensorTumb(findNode("Tumbler"))
#tsensor1 = createTouchSensor1(findNode("1"))
#tsensor2 = createTouchSensor2(findNode("2"))
#tsensor3 = createTouchSensor3(findNode("3"))
#tsensor4 = createTouchSensor4(findNode("4"))
#tsensor5 = createTouchSensor5(findNode("5"))
#tsensor6 = createTouchSensor6(findNode("6"))
tsensor8 = createTouchSensor8(findNode("8"))
tsensorMove_Tumb = createTouchSensorMov_Tumb(findNode("moving_Tumbler1"))
tsensor_t_i = createTouchSensorMov_thu_ind(findNode("moving_Tumbler1"))

#tsensorDeact = createTouchSensorDeact(findNode("deactive"))


# The update will force the touch sensors UI to refresh
vrController.updateTouchSensors()