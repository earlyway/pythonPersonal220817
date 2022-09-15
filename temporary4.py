sys.path.append("c:/Users/Tium/Documents/pythonPersonal220817")
import time, sys
from Vector import *


calcVertexNormals()
clearFindCache()
updateScene()

class GetNode():
    def __init__(self):
        pass
    def SetPathList(self, step3):
        pathCoordi = []
        pathLineNode = None
        boxAmount = 0
        pathLineNode = step3.getChild(1)
        boxAmount = pathLineNode.getNChildren()
        print('boxAmount2 : ' + str(boxAmount)) #10이 나와야함
        for i in range(boxAmount):
            pathCoordi.append(pathLineNode.getChild(i).getWorldTranslation())
        print('pathCoordi : ' + str(pathCoordi))
        print('pathCoordi len : ' +str(len(pathCoordi)))
        return pathCoordi


class MainLoop():
    #NodePar = None
    #fnPCount = None
    CurveList = []

    def __init__(self):
        pass
    def RunFind(self, nodeNum):
        print('nodeNum1 ' + str(nodeNum))
        nodeNum=findNode(nodeNum) # findNode로 인해 vrNodePtr형태로 return된 nodeNum.
        #이 vrNodePtr형태가 아니면 바로 아래 라인의 getNChildren 메서드를 쓸 수 없음
        #print('nodeNum2 ' + str(nodeNum))
        #fnPCount = nodeNum.getNChildren()
        #print('fnPCount1 : '+str(fnPCount))   # 1
        #for i in range(fnPCount):
        #    self.nodeNum = nodeNum
        #    print('nodeNum3 '+ str(nodeNum))
        #    getN = GetNode()
        #    ff = getN.SetPathList(self.nodeNum.getChild(i)) #여기서 self.nodeNum 는 vrNodePtr 형태임. GetChild 메서드를 쓰기위함.
        #    self.CurveList.append(ff)

        getN = GetNode()
        ff = getN.SetPathList(nodeNum.getChild(0)) #여기서 self.nodeNum 는 vrNodePtr 형태임. GetChild 메서드를 쓰기위함.
        self.CurveList.append(ff)


ml = MainLoop()


findNodeOrigin = findNode('origin')
findNodeOriginAmount = findNodeOrigin.getNChildren() # 6 return

for i in range(findNodeOriginAmount):
    findNodeNumName = findNodeOrigin.getChild(i).getName()
    print('firstNodeNum '+ str(findNodeNumName))
    ml.RunFind(findNodeNumName)

print(len(ml.CurveList))
print(len(ml.CurveList[0][0])) # 3 return.
print(str(ml.CurveList))
print('===3===================================================')
