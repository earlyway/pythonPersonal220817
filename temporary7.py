#220921 originA 스크립트를 만들기 위한 임시파일

#220919
clearScript()
clearFindCache()

sys.path.append("C:/Users/Tium/Documents/pythonPersonal220817/")
import Curve, Vector, time, Test_VMainLoop, Test_VNode
from Vector import *
from Test_VMainLoop import *
from Test_VNode import *

loadGeometry("$VRED_EXAMPLES/geo/boxlist5.osb")
#loadGeometry("$VRED_EXAMPLES/geo/boxlist6.osb")

#-----------------------------moving 오브젝트를 직접 씬에 load

calcVertexNormals()

#-----------------------------
class ori():
    def __init__(self):
        pass

    def findOri(self, oriNum):
        global CurveList
        CurveList = None

        findNodeOrigin = findNode(oriNum)
        findNodeOriginAmount = findNodeOrigin.getNChildren() #
        print('findNodeOriginAmount ' + str(findNodeOriginAmount))
        #-----------------------------

        ml = Test_VMainLoop.MainLoop() #find in scene Path
        ml.pathCoordiListA = []
        #-----------------------------Node In Get Points
        for i in range(findNodeOriginAmount):
            findNodeNumName = findNodeOrigin.getChild(i).getName() #origin 노드의 하위 노드 이름을 가져옴.
            print('findNodeNumName ' + str(findNodeNumName))
            show = ml.RunFindA(findNodeNumName)


        #-----------------------------


        print(len(ml.pathCoordiListA)) #3
        print(len(ml.pathCoordiListA[0])) #10

        print('=====3=================================================')

        #----------------------------------------

        #미리 생성된 pathCube들의 월드좌표들을 CurveList 배열에 엘레멘트로 추가함.

        CurveList = Curve.BezierCurve3D()
        CurveList.Call()

        CurveList.linePoints = []
        #----------------------------------------

        cubeAmount2 = findNode('Path')
        cubeAmount22 = cubeAmount2.getNChildren() # Path 노드의 하위 노드 개수를 가져옴

        #----------------------------------------

        for i in range(findNodeOriginAmount):
            for j in range(cubeAmount22):
                CurveList.AddPointLine((ml.pathCoordiListA[i][j]))
                #AddPointLine 메서드에 의해 pathCoordiList[i][j]의 모든 엘레멘트들이 linePoints 하나의 배열에 들어감.
        print('CurveList' + str(CurveList.linePoints))

fo = ori()
print('-------A')
fo.findOri('originA')

class TestAction(vrAEBase): #TestAction 클래스에서 deltaTime을 적용.
    target = None
    path = []
    index = 0
    pathCount = 0
    #lookAt = (0.0, 0.0, 0.0)

    #setDir = 0.0
    pathTime = 0.0
    deltaTime = 0.0 #델타타임 생성
    lastFrameTime = 0.0

    speed = 0.25 #moving 오브젝트가 pathCube에서 다음 pathCube로 넘어가기까지의 속도 조절

    #stType = false

    def __init__(self):
        vrAEBase.__init__(self)
        print('TestAction on')
        self.addLoop() # 객체가 호출함과 동시에 Loop 추가+loop메서드 실행.

    def SetTarget(self, setTarget, setPath): # 인자를 받아 setTarget, setPath에 대입.
        #setTarget 인자는 moving 오브젝트를 가리키고
        #setPath는 pathCube의 월드좌표가 엘레멘트로 있는 linePoints 배열을 가리킴.
        print('SetTarget')
        self.target = setTarget
        self.path = setPath
        self.pathCount = len(setPath)-1 # pathCube의 개수-1 을 pathCount 변수에 할당.

    def recEvent(self, state):
        vrAEBase.recEvent(self, state)
        print('recEvent on')

    def loop(self): # __init__ 로 인해 loop문 메서드가 실행될것.
        print('loop method start')
        curNode = None
        if self.lastFrameTime == 0.0:
            self.lastFrameTime = time.time() # python 라이브러리의 time 을 가져와서 lastFrameTime에 할당

        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastFrameTime # 현재시간-마지막 frame의 시간

        if self.deltaTime > 1:
            pass
        else: #deltaTime <= 1 일때,
            if self.pathTime < 1: #pathTime이 의미하는 것은 무엇일까??
                #그리고 위에서 pathTime을 이미 0 으로 초기화했기때문에 처음에 if문을 무조건 거쳐가게 됨.
                self.pathTime = self.pathTime + self.deltaTime * self.speed
                self.index = int(Vector1.Lerp(0, self.pathCount, self.pathTime))
                #Vector.py의 Vector1 class의 Lerp메서드를 호출. startPos, endPos, t 를 인자로 넘기고
                #int(startPos*(1.0-t) + endPos*t) 값으로 return.
                if self.pathTime >= 1: # pathTime이 1보다 크거나 같으면 pathTime, index, lookat 초기화.
                    self.pathTime = 0.0
                    self.index = 0 #index가 의미하는 바는?
                    #self.lookAt = (0.0, 0.0, 0.0)
            else:  #pathTime >= 1 일때,
                self.pathTime = 0.0
                self.index = 0
                #self.lookAt = (0.0, 0.0, 0.0)

            #-----------
            curNode = CurveList.linePoints[self.index]
            print('curNode : ' + str(curNode))
            #curPoint = curNode[self.index]
            #print('curPoint : ' + str(curPoint))
            self.target.setWorldTranslation(curNode[0], curNode[1], curNode[2]) # linePoints 배열의 index(좌표 정보)를 가져와 좌표에 대치시킴
            #self.target = moveObje
            #if self.stType == false:
            # 회전은 수학 공식에 문제가 있으니 나중에
            #if self.index < self.pathCount - 1:
            #setdir = Vector3.Lookat(self.path[self.index], self.path[self.index + 1])
            #self.lookAt = Vector3.Add(self.lookAt, setdir)
            #self.target.setRotation(0.0, 0.0, self.lookAt[2])

        self.lastFrameTime = self.currentTime

    #----------------------------loop 메서드 끝----
    def loopStop(self):
        print('loop method end')
        self.subLoop() #add된 loop를 substract함.

#-----------------------------------------------------------------------------------

keyO = vrKey(Key_O) # 영어 O 키입력을 감지

moveObjec = findNode("Cube99") # load된 boxList5.osb 에 있는 Cube99 노드를 찾아 moveObjec변수에 할당
moveObjec.makeTransform()   #찾은 노드를 transform 가능한 상태로 변환(변환해야 s, t, r 를 바꿀 수 있음).
setTransformNodeScale(moveObjec,0.05,0.05,0.05) #변환된 노드의 scale을 setting.
#setdir = CurveList.linePoints[0]
#moveObjec.setTranslation(setdir[0], setdir[1], setdir[2])


cm = TestAction() #TestAction class를 호출하는 cm객체
#cm.stType = false
cm.SetTarget(moveObjec, CurveList.linePoints) # SetTarget 메서드에 인자를 넘기는 cm객체.
cm.setActive(true) #cm객체를 위한 렌더링을 활성화.
#그러면 cm = TestAction() 이 문구가 또 실행되는건가?

keyO.connect(cm.loopStop)
