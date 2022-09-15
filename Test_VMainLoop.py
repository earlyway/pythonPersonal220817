import Vector
import vrScenegraph
import Test_VNode as VN
from Vector import *
from Test_VNode import *

class MainLoop():
    CurveList = []
    def __init__(self):
        pass
    def RunFind(self, nodeNum):
        nodeNum = vrScenegraph.findNode(nodeNum) 
        getN = VN.GetNode()
        ff = getN.SetPathList(nodeNum.getChild(0))
        self.CurveList.append(ff)
        
    def testing(self,dn):
        print('dn : ' + str(dn))

