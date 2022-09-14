class GetNode():
    def __init__(self):
        pass
    
    def SetPathList(self, node):
        rtPath = []
        getRoot = node.getChild(0).getChild(1)
        boxCount = getRoot.getNChildren()  #gets the number of children
        print('boxCount2 : ' + str(boxCount))
        for i in range(boxCount):
            rtPath.append(getRoot.getChild(i))

        return rtPath