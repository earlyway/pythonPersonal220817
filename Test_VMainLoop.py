# #import Vector, VrNode
# import vrScenegraph
# import VrNode as Vr
# from Vector import *
# from VrNode import *

# class MainLoop():
#     def __init__(self):
#         pass
    
#     def RunFind(self, pa):
#         NodePar = vrScenegraph.findNode(pa)
#         fnPCount = NodePar.getNChildren() #gets the number of children
#         print('fnPCount1 : '+str(fnPCount))

#         for i in range(fnPCount):
#             ti = Vr.GetNode()
#             fn = ti.SetPathList(NodePar.getChild(i))
#             self.CurveList.append(fn)
#-------------------------------------------------------------------------
import Vector
import vrScenegraph, vrNodePtr
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

