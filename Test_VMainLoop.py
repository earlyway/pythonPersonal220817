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
    def RunFind(self, nodeNum): #nodeNum 은 Group5, 6, 7 올것
        pathCoordiList = []
        nodeNum = vrScenegraph.findNode(nodeNum)
        getN = VN.GetNode()         #Test_VNode.py 호출
        return getN.SetPathList(nodeNum.getChild(0))


                            #nodeNum.getChild(0) 은 straight1 node
    def RunFindA(self, nodeNum): #nodeNum 은 Group5, 6, 7 올것
        pathCoordiListA = []
        nodeNum = vrScenegraph.findNode(nodeNum)
        getN = VN.GetNode()         #Test_VNode.py 호출
        return getN.SetPathList(nodeNum.getChild(0))
