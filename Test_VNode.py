# class GetNode():
#     def __init__(self):
#         pass
    
    
#     def SetPathList(self, node):
#         rtPath = []
#         getRoot = node.getChild(0).getChild(1)
#         boxCount = getRoot.getNChildren()  #gets the number of children
#         print('boxCount2 : ' + str(boxCount))
#         for i in range(boxCount):
#             rtPath.append(getRoot.getChild(i))

#         return rtPath
#--------------------------------------------------------------------------
class GetNode():
    def __init__(self):
        pass
    def SetPathList(self, step3):
        pathCoordi = []
        pathLineNode = None
        boxAmount = 0
        pathLineNode = step3.getChild(1)
        boxAmount = pathLineNode.getNChildren()

        for i in range(boxAmount):
            pathCoordi.append(pathLineNode.getChild(i).getWorldTranslation())
        return pathCoordi