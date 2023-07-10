class GetNode(): #Test_VMainLoop.py에서 쓰일 class
    def __init__(self):
        pass
    def SetPathList(self, step3):
        pathCoordi = []
        pathLineNode = None
        boxAmount = 0
        pathLineNode = step3.getChild(1)
        #step3.getChild(1) 은 Group5의 straight1의 Path3 노드
        boxAmount = pathLineNode.getNChildren()
        #pathLineNode.getNChildren() 은 Group5의 straight1의 Path3 노드의 하위 자식 개수.

        for i in range(boxAmount):
            pathCoordi.append(pathLineNode.getChild(i))
        return pathCoordi   #pathCoordi 는 list형