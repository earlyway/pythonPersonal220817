#220922

#220921 originA 스크립트를 만들기 위한 임시파일

#220919
clearScript()
clearFindCache()

sys.path.append("C:/Users/Tium/Documents/pythonPersonal220817/")
import Curve, Vector, time, Test_VMainLoop, Test_VNode
from Vector import *
from Test_VMainLoop import *
from Test_VNode import *

#-----------------------------moving 오브젝트를 직접 씬에 load

calcVertexNormals()

CurveListA = []
CurveListB = []
CurveListC = []

#-----------------------------
class ori():
    def __init__(self):
        pass

    def findOri(self, oriNum):

        findNodeOrigin = findNode(oriNum)
        findNodeOriginAmount = findNodeOrigin.getNChildren() #
        #-----------------------------

        ml = Test_VMainLoop.MainLoop() #find in scene Path

        # if oriNum == "originA":
        #     ml.pathCoordiListA = []
        #
        #     for i in range(findNodeOriginAmount):
        #         findNodeNumName = findNodeOrigin.getChild(i).getName() #origin 노드의 하위 노드 이름을 가져옴.
        #         ml.RunFindA(findNodeNumName)

        if oriNum == "originB":
            ml.pathCoordiListB = []

            for i in range(findNodeOriginAmount):
                findNodeNumName = findNodeOrigin.getChild(i).getName() #origin 노드의 하위 노드 이름을 가져옴.
                ml.RunFindB(findNodeNumName)

        # elif oriNum == "originC":
        #     ml.pathCoordiListC = []
        #
        #     for i in range(findNodeOriginAmount):
        #         findNodeNumName = findNodeOrigin.getChild(i).getName() #origin 노드의 하위 노드 이름을 가져옴.
        #         ml.RunFindC(findNodeNumName)
        else:
            print("Find null")

        #----------------------------------------
        cubeAmount2 = findNode('Path')
        cubeAmount22 = cubeAmount2.getNChildren() # Path 노드의 하위 노드 개수를 가져옴
        #----------------------------------------

        # if oriNum == "originA":
        #     for i in range(findNodeOriginAmount):
        #         for j in range(cubeAmount22):
        #             CurveListA.append(ml.pathCoordiListA[i][j])

        if oriNum == "originB":
            for i in range(findNodeOriginAmount):
                for j in range(cubeAmount22):
                    CurveListB.append(ml.pathCoordiListB[i][j])

        # elif oriNum == "originC":
        #     for i in range(findNodeOriginAmount):
        #         for j in range(cubeAmount22):
        #             CurveListC.append(ml.pathCoordiListC[i][j])

        else:
            print("Error")

#--------------------------------------------------

rootA = ori()
rootA.findOri('originA')

rootB = ori()
rootB.findOri('originB')

rootC = ori()
rootC.findOri('originC')

#--------------------------------------------------

class TestAction(vrAEBase): #TestAction 클래스에서 deltaTime을 적용.
    target = None
    path = []
    index = 0
    pathCount = 0

    pathTime = 0.0
    deltaTime = 0.0 #델타타임 생성
    lastFrameTime = 0.0

    speed = 0.25 #moving 오브젝트가 pathCube에서 다음 pathCube로 넘어가기까지의 속도 조절

    def __init__(self):
        vrAEBase.__init__(self)
        print('1')
        self.addLoop() # 객체가 호출함과 동시에 Loop 추가+loop메서드 실행.

    def SetTarget(self, setTarget, setPath): # 인자를 받아 setTarget, setPath에 대입.
        print('2')
        self.target = setTarget
        self.path = setPath
        self.pathCount = len(setPath)-1 # pathCube의 개수-1 을 pathCount 변수에 할당.

    def recEvent(self, state):
        vrAEBase.recEvent(self, state)

    def loop(self): # __init__ 로 인해 loop문 메서드가 실행될것.
        print('3')
        curNode = None
        if self.lastFrameTime == 0.0:
            self.lastFrameTime = time.time() # python 라이브러리의 time 을 가져와서 lastFrameTime에 할당

        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastFrameTime # 현재시간-마지막 frame의 시간

        if self.deltaTime > 1:
            pass
        else: #deltaTime <= 1 일때,
            if self.pathTime < 1: #pathTime이 의미하는 것은 무엇일까??
                self.pathTime = self.pathTime + self.deltaTime * self.speed
                self.index = int(Vector1.Lerp(0, self.pathCount, self.pathTime))
                if self.pathTime >= 1: # pathTime이 1보다 크거나 같으면 pathTime, index, lookat 초기화.
                    self.pathTime = 0.0
                    self.index = 0 #index가 의미하는 바는?
            else:  #pathTime >= 1 일때,
                self.pathTime = 0.0
                self.index = 0

            #------------------------------------------------

            #self.path 는 CurveListA, B, C의 모든 path값이 있을것
            curNode = self.path[self.index] #path 는 CurveListA,B,C 의 엘레멘트를 가져옴.

            curPos = curNode.getWorldTranslation()
            curRot = curNode.getWorldRotation()
            self.target.setWorldTranslation(curNode[0], curNode[1], curNode[2]) # linePoints 배열의 index(좌표 정보)를 가져와 좌표에 대치시킴
            self.target.setRotation(curRot[0], curRot[1], curRot[2]) # linePoints 배열의 index(좌표 정보)를 가져와 좌표에 대치시킴

        self.lastFrameTime = self.currentTime

    #----------------------------loop 메서드 끝----

    def loopStop(self):
        print('loop method end')
        self.subLoop() #add된 loop를 substract함.

#-----------------------------------------------------------------------------------

keyO = vrKey(Key_O) # 영어 O 키입력을 감지

# moveObjecA = findNode("Cube99") # load된 boxList5.osb 에 있는 Cube99 노드를 찾아 moveObjec변수에 할당
# cmA = TestAction() #TestAction class를 호출하는 cm객체
# cmA.SetTarget(moveObjecA, CurveListA) # SetTarget 메서드에 인자를 넘기는 cm객체.
# cmA.setActive(true) #cm객체를 위한 렌더링을 활성화.

moveObjecB = findNode("Cube100") # load된 boxList5.osb 에 있는 Cube99 노드를 찾아 moveObjec변수에 할당
cmB = TestAction() #TestAction class를 호출하는 cm객체
cmB.SetTarget(moveObjecB, CurveListB) # SetTarget 메서드에 인자를 넘기는 cm객체.
cmB.setActive(true) #cm객체를 위한 렌더링을 활성화.

# moveObjecC = findNode("Cube101") # load된 boxList5.osb 에 있는 Cube99 노드를 찾아 moveObjec변수에 할당
# cmC = TestAction() #TestAction class를 호출하는 cm객체
# cmC.SetTarget(moveObjecC, CurveListC) # SetTarget 메서드에 인자를 넘기는 cm객체.
# cmC.setActive(true) #cm객체를 위한 렌더링을 활성화.

# keyO.connect(cmA.loopStop)
keyO.connect(cmB.loopStop)
# keyO.connect(cmC.loopStop)