import Vector
import vrScenegraph
import Test_VNode as VN
from Vector import *
from Test_VNode import *

class MainLoop():
    pathCoordiList = []
    def __init__(self):
        pass
    def RunFind(self, nodeNum):
        nodeNum = vrScenegraph.findNode(nodeNum)
        getN = VN.GetNode()
        ff = getN.SetPathList(nodeNum.getChild(0))
        self.pathCoordiList.append(ff)

