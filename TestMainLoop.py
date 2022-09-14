#import Vector, VrNode
import vrScenegraph
import VrNode as Vr
from Vector import *
from VrNode import *

class MainLoop():
    def __init__(self):
        pass
    
    def RunFind(self, pa):
        NodePar = vrScenegraph.findNode(pa)
        fnPCount = NodePar.getNChildren() #gets the number of children
        print('fnPCount1 : '+str(fnPCount))

        for i in range(fnPCount):
            ti = Vr.GetNode()
            fn = ti.SetPathList(NodePar.getChild(i))
            self.CurveList.append(fn)
        
