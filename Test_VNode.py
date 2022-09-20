class GetNode():
    def __init__(self):
        pass
    def SetPathList(self, step3):
        pathCoordi = []
        pathLineNode = None
        boxAmount = 0
        pathLineNode = step3.getChild(1)
        boxAmount = pathLineNode.getNChildren()
        print('boxAmount ' + str(boxAmount))

        for i in range(boxAmount):
            pathCoordi.append(pathLineNode.getChild(i).getWorldTranslation())
        return pathCoordi