# 커브라인과 직선라인을 합치는 작업 완료
# 이동 오브젝트를 speedshape에서 boxcube로 바꾸었고 scale을 크게 키움. 초반 시작 시, 로딩이 많이 걸림
# 이동 오브젝트에 알파채널을 끄고 새로 파일 저장->적용 완료
sys.path.append("C:/Users/Tium/Documents/pythonPersonal220817/")
import Curve, Vector, time
from Vector import *

loadGeometry("$VRED_EXAMPLES/geo/boxlist5.osb")
loadGeometry("$VRED_EXAMPLES/geo/boxlist6.osb")
#-----------------------------moving 오브젝트를 직접 씬에 load
calcVertexNormals()

CurveList = Curve.BezierCurve3D()
CurveList.Call()

StraightList = Curve.BezierCurve3D()
StraightList.Call()

CurveList.points = []
CurveList.AddPoint((-2500,900,850))
CurveList.AddPoint((300, 900, 850))
CurveList.AddPoint((900, 900, 850))
CurveList.AddPoint((900, 600, 850))
CurveList.AddPoint((900, -1500, 850))

StraightList.points = []
StraightList.AddPoint((-2500,900,850))
StraightList.AddPoint((4500,900,850))


size = 40
count = 90
CurveList.linePoints = []
for i in range(count):
    CurveList.linePoints.append(CurveList.CurveA(i/count))
    node = vrNodeUtils.createBox(size, size, size, 1, 1, 1, 1, 1, 1, 0)
    node.makeTransform()
    node.setTranslation(CurveList.GetlinePointX(i), CurveList.GetlinePointY(i), CurveList.GetlinePointZ(i))

StraightList.linePoints = []
for i in range(count):
    StraightList.linePoints.append(StraightList.CurveA(i/count))
    nodeST = vrNodeUtils.createBox(size, size, size, 1, 1, 1, 1, 1, 1, 0)
    nodeST.makeTransform()
    nodeST.setTranslation(StraightList.GetlinePointXst(i), StraightList.GetlinePointYst(i), StraightList.GetlinePointZst(i))



updateScene()
#----------------------------------------
#미리 생성된 pathCube들의 월드좌표들을 CurveList 배열에 엘레멘트로 추가함.
#

class TestAction(vrAEBase): #TestAction 클래스에서 deltaTime을 적용.
    target = None
    path = []
    index = 0
    pathCount = 0
    lookAt = (0.0, 0.0, 0.0)

    setDir = 0.0
    pathTime = 0.0
    deltaTime = 0.0
    lastFrameTime = 0.0

    speed = 0.25

    stType = false

    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()

    def SetTarget(self, setTarget, setPath):
        self.target = setTarget
        self.path = setPath
        self.pathCount = len(setPath)-1

    def recEvent(self, state):
        vrAEBase.recEvent(self, state)

    def loop(self):
        if self.lastFrameTime == 0.0:
            self.lastFrameTime = time.time()

        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastFrameTime

        if self.deltaTime > 1:
            pass
        else:
            if self.pathTime < 1:
                self.pathTime = self.pathTime + self.deltaTime * self.speed
                self.index = int(Vector1.Lerp(0, self.pathCount, self.pathTime))
                if self.pathTime >= 1:
                    self.pathTime = 0.0
                    self.index = 0
                    self.lookAt = (0.0, 0.0, 0.0)
            else:
                self.pathTime = 0.0
                self.index = 0
                self.lookAt = (0.0, 0.0, 0.0)

            StraightList = self.path[self.index]
            self.target.setWorldTranslation(StraightList[0], StraightList[1], StraightList[2])
            #-----------
            if self.stType == false:
                # 회전은 수학 공식에 문제가 있으니 나중에
                if self.index < self.pathCount - 1:
                    setdir = Vector3.Lookat(self.path[self.index], self.path[self.index + 1])
                    self.lookAt = Vector3.Add(self.lookAt, setdir)
                    self.target.setRotation(0.0, 0.0, self.lookAt[2])

        self.lastFrameTime = self.currentTime

    def loopStop(self):
        self.subLoop() #add된 loop를 substract함.

#-----------------------------------------------------------------------------------

keyI = vrKey(Key_I)

car = findNode("Cube99")
car.makeTransform()
setTransformNodeScale(car,1,1,1)
setdir = CurveList.linePoints[0]
car.setTranslation(setdir[0], setdir[1], setdir[2])

cm = TestAction()
cm.stType = false
cm.SetTarget(car, CurveList.linePoints)
cm.setActive(true)

keyI.connect(cm.loopStop)
#load된 moving 오브젝트의 앞방향 진행경로를 설정해주고
#SetTarget에서 pathCube의 월드좌표를 가져와 대치시키면서 moving 진행하는듯.
#-----------------------------------------------------------------------------------

carST = findNode("Cube100")
carST.makeTransform()
setTransformNodeScale(carST,1,1,1)
setdirST = StraightList.linePoints[0]
carST.setTranslation(setdirST[0], setdirST[1], setdirST[2])

cmST = TestAction()
cmST.stType = true
cmST.SetTarget(carST, StraightList.linePoints)
cmST.setActive(true)

keyI.connect(cmST.loopStop)