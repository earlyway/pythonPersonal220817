import Vector
import vrScenegraph
import Test_VNode as VN
from Vector import *
from Test_VNode import *

class MainLoop():
    nodeNum = None
    getN = None
    
    def __init__(self):
        pass
    def RunFind(self, nodeNum):
        pathCoordiList = []
        nodeNum = vrScenegraph.findNode(nodeNum)
        getN = VN.GetNode()
        return getN.SetPathList(nodeNum.getChild(0))
