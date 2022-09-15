#220901

# class Action():
#
#     def __init__(self):
#         self.addLoop()
#
#
#     def loop(self):
#         if self.my = 0 : #1로 가도록
#             self.zero = findMaterial("VredAlpha")
#             self.zero.setTransparency(1.0)
#             self.subLoop()
#         else :
#             pass
#
#
#
# #------------
# my = findMaterial.getTransparency("VredAlpha")
#
# aaa = Action()
# #aaa = findMaterial("VredAlpha")
# aaa.loop(my)
# print(dir(aaa))
# #aaa.setTransparency(0.0)
#
#
# ------------------- while 문으로 0to1 해보자
# import time
# class Action():
#     count = 0
#     lastFrameTime = 0
#     createTime = 0
#     #my = 0
#
#     def __init__(self):
#         self.addLoop()
#
#
#     def loop(self):
#         self.currentTime = time.time()
#         self.deltaTime = self.currentTime - self.lastFrameTime
#         self.createTime += self.deltaTime
#
#         while self.my == 0 :
#             self.count = self.count + 0.05
#             self.my += self.count
#
#             if self.my == 1 :
#                 self.subLoop()
#                 break
#
#
#
#
# #------------
# my = findMaterial.getTransparency("VredAlpha")
#
# aaa = Action()
# #aaa = findMaterial("VredAlpha")
# aaa.loop(my)
# print(dir(aaa))
# #aaa.setTransparency(0.0)

#-----------------------220901설계해놓은대로 코딩해보자

sys.path.append("C:/Users/Tium/Documents/pythonPersonal220817/")
import Curve, Vector, time
from Vector import *

loadGeometry("$VRED_EXAMPLES/geo/boxlist5.osb")
loadGeometry("$VRED_EXAMPLES/geo/boxlist6.osb")

calcVertexNormals()

CurveList = Curve.BezierCurve3D()
StraightList = Curve.BezierCurve3D()


class RailRoad(vrAEBase):




    def __init__(self):
        vrAEBase.__init__(self)
        self.addLoop()


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

            if self.stType == false:
                # 회전은 수학 공식에 문제가 있으니
                if self.index < self.pathCount - 1:
                    setdir = Vector3.Lookat(self.path[self.index], self.path[self.index + 1])
                    self.lookAt = Vector3.Add(self.lookAt, setdir)
                    self.target.setRotation(0.0, 0.0, self.lookAt[2])

        self.lastFrameTime = self.currentTime

    def loopStop(self):
        self.subLoop()

#---------------------------

#1.배치된 레일의 패스 포인트를 파악한다.
keyI = vrKey(Key_I)

car = findNode("Cube99")
#car.makeTransform()
setTransformNodeScale(car,10,10,10)
setdir = CurveList.linePoints[0]
car.setTranslation(setdir[0], setdir[1], setdir[2])


cm = TestAction()
cm.stType = False
cm.SetTarget(car, CurveList.linePoints)
cm.setActive(true)

keyI.connect(cm.loopStop)

#--------------------------

carST = findNode("Cube100")
#carST.makeTransform()
setTransformNodeScale(carST,10,10,10)
setdirST = StraightList.linePoints[0]
carST.setTranslation(setdirST[0], setdirST[1], setdirST[2])


cmST = TestAction()
cmST.stType = True
cmST.SetTarget(carST, StraightList.linePoints)
cmST.setActive(true)

keyI.connect(cmST.loopStop)







#→ 직선 레일과 커브 레일을 이용해서 생산 라인을 배치한다.
#>스크립트를 실행
#>배치된 레일의 패스 포인트를 파악한다. find rail3d-select rail3d-getposition(여기서 시작점, 끝점이 파악되어야함.)
#>패스 포인트를 바탕으로 패스 정보를 저장한다.
#>패스 정보를 토대로 각 레일의 시작점과 끝점을 하나로 통합한다.
#>통합된 패스 정보대로 패스 큐브를 생성한다.
#>moving 오브젝트를 움직이게 한다.





















