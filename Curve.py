# https://www.icode.com/c-function-for-a-bezier-curve/ C# 4포인트 베지어 곡선 예제
# https://starrykss.tistory.com/1843 3포인트 베지어 곡선 예제
# https://blog.coderifleman.com/2016/12/30/bezier-curves/ 
# https://ko.javascript.info/bezier-curve
# https://rito15.github.io/posts/unity-study-bezier-curve/
# https://en.wikipedia.org/wiki/B%C3%A9zier_curve 위키
# https://lee-seokhyun.gitbook.io/workspace/client/easy-mathematics/gdc2012/3

# https://hwikiko.cyou/wiki/b%c3%a9zier_curve#Higher-order_curves  N차 베지어곡선 예제
# https://kr.mathworks.com/help/matlab/ref/polyfit.html
# https://www.youtube.com/watch?v=uRhe_A4DWPA
# https://blog.naver.com/kyuniitale/40022945907
# https://ytyt.github.io/siiiimple-bezier/ bezier curve simulator

import Vector
# import tkinter
from Vector import *
# from tkinter import *

#----------------------------------------------------------------------------------------------------------------

# 끝점과 처음점이 연결안된 커브 구현 N차 베지어곡선
class BezierCurve2D():
    points = []
    linePoints = []
    # closed = False

    def __init__(self):
        pass
    def __del__(self):
        pass

    def Call(self):
        print("BezierCurve2D Call")
        
    def Call2(self):
        print("BezierCurve2D Call 22")
        
    def Call3(self, a):
        print('BezierCurve2D Call 333'+str(a))
        
    def AddPoint(self, vector2):
        self.points.append(vector2)

    def GetPoints(self):
        return self.points

    def ValueLerp(self, startPos, endPos, t):
        return (startPos * (1.0 - t) + endPos * t)

    def GetPoint(self, t, vt2p0, vt2p1, vt2p2):
        p1 = Vector2.Lerp(vt2p0, vt2p1, t)
        p2 = Vector2.Lerp(vt2p1, vt2p2, t)
        return Vector2.Lerp(p1, p2, t)

    # N차 베지어곡선 코드
    def GetCurvePoint(self, t):
        if t == 1:
            return self.points[len(self.points)-1]
        else:
            cp = self.points
            cunnetLines = len(cp)-1
            while cunnetLines > 2:
                cp2 = []
                for c in range(cunnetLines):
                    cp2.append(Vector2.Lerp(cp[c], cp[c+1], t))
                cp = cp2
                cunnetLines = cunnetLines - 1

            return self.GetPoint(t, cp[0], cp[c], cp[2])

    def CurveA(self, t):
        if len(self.points) == 0:
            pass
        elif len(self.points) == 1:
            pass
        elif len(self.points) == 2:
            return Vector2.Lerp(self.points[0], self.points[1], t)
        elif len(self.points) == 3:
            return self.GetPoint(t, self.points[0], self.points[1], self.points[2])
        else: # N차 베지어 곡선
            return self.GetCurvePoint(t)
        
    def CreateCurve(self, count):
        for i in range(count):
            self.curvePoint.append(self.CurveA(i/count))
        
# N차 베지어곡선 코드 Helf
    def GetCurvePointHelf(self, t):
        if t == 1:
            return self.points[len(self.points)-1]
        else:
            cp = self.points
            cunnetLines = len(self.points)-2

            if (len(self.points) % 2) == 0:
                while cunnetLines > 2:
                    cp2 = []
                    for c in range(cunnetLines):
                        cp2.append(self.GetPoint(t, cp[c], cp[c+1], cp[c+2]))
                    cp = cp2
                    cunnetLines = len(cp)-2

                cnLine1 = self.GetPoint(t, cp[0], cp[1], cp[2])
                cnLine2 = self.GetPoint(t, cp[1], cp[2], cp[3])
                return Vector2.Lerp(cnLine1, cnLine2, t)
            else:
                while cunnetLines > 1:
                    cp2 = []
                    for c in range(cunnetLines):
                        cp2.append(self.GetPoint(t, cp[c], cp[c+1], cp[c+2]))
                    cp = cp2
                    cunnetLines = len(cp)-2

                return self.GetPoint(t, cp[0], cp[1], cp[2])

    def CurveHelf(self, t):
        if len(self.points) == 2:
            return Vector2.Lerp(self.points[0], self.points[1], t)
        elif len(self.points) == 3:
            return self.GetPoint(t, self.points[0], self.points[1], self.points[2])
        else: # N차 베지어 곡선
            return self.GetCurvePointHelf(t)

    def CreateCurveHelf(self, count):
        for i in range(count):
            self.curvePoint.append(self.CurveHelf(i/count))
            
    def Closed(self):
        self.points.append(self.points[0])

#----------------------------------------------------------------------------------------------------------------

class BezierCurve3D():
    points = []
    linePoints = []
    # closed = False

    def __init__(self):
        pass
    def __del__(self):
        pass
    
    def Call(self):
        print("BezierCurve3D Call")

    def AddPoint(self, vector3):
        self.points.append(vector3)
        
    def AddPointLine(self, vect3):
        self.linePoints.append(vect3)

    def GetPoints(self):
        return self.points

    def ValueLerp(self, startPos, endPos, t):
        return (startPos * (1.0 - t) + endPos * t)
    
    def GetlinePoint(self, index):
        return self.linePoints[index]
    
    def GetlinePointX(self, index):
        CurveList = self.linePoints[index]
        return CurveList[0]
    
    def GetlinePointY(self, index):
        CurveList = self.linePoints[index]
        return CurveList[1]
    
    def GetlinePointZ(self, index):
        CurveList = self.linePoints[index]
        return CurveList[2]
    
    
    def GetlinePointXst(self, index):
        StraightList = self.linePoints[index]
        return StraightList[0]
    
    def GetlinePointYst(self, index):
        StraightList = self.linePoints[index]
        return StraightList[1]
    
    def GetlinePointZst(self, index):
        StraightList = self.linePoints[index]
        return StraightList[2]
    
    
    def GetPoint(self, t, vt2p0, vt2p1, vt2p2):
        p1 = Vector3.Lerp(vt2p0, vt2p1, t)
        p2 = Vector3.Lerp(vt2p1, vt2p2, t)
        return Vector3.Lerp(p1, p2, t)

    # N차 베지어곡선 코드
    def GetCurvePoint(self, t):
        if t == 1:
            return self.points[len(self.points)-1]
        else:
            cp = self.points
            cunnetLines = len(cp)-1
            while cunnetLines > 2:
                cp2 = []
                for c in range(cunnetLines):
                    cp2.append(Vector3.Lerp(cp[c], cp[c+1], t))
                cp = cp2
                cunnetLines = cunnetLines - 1

            return self.GetPoint(t, cp[0], cp[c], cp[2])

    def CurveA(self, t):
        if len(self.points) == 0:
            pass
        elif len(self.points) == 1:
            pass
        elif len(self.points) == 2:
            return Vector3.Lerp(self.points[0], self.points[1], t)
        elif len(self.points) == 3:
            return self.GetPoint(t, self.points[0], self.points[1], self.points[2])
        else: # N차 베지어 곡선
            return self.GetCurvePoint(t)
    def CreateCurve(self, count):
        for i in range(count):
            self.curvePoint.append(self.CurveA(i/count))

         # N차 베지어곡선 코드 Helf
    def GetCurvePointHelf(self, t):
        if t == 1:
            return self.points[len(self.points)-1]
        else:
            cp = self.points
            cunnetLines = len(self.points)-2

            if (len(self.points) % 2) == 0:
                while cunnetLines > 2:
                    cp2 = []
                    for c in range(cunnetLines):
                        cp2.append(self.GetPoint(t, cp[c], cp[c+1], cp[c+2]))
                    cp = cp2
                    cunnetLines = len(cp)-2

                cnLine1 = self.GetPoint(t, cp[0], cp[1], cp[2])
                cnLine2 = self.GetPoint(t, cp[1], cp[2], cp[3])
                return Vector3.Lerp(cnLine1, cnLine2, t)
            else:
                while cunnetLines > 1:
                    cp2 = []
                    for c in range(cunnetLines):
                        cp2.append(self.GetPoint(t, cp[c], cp[c+1], cp[c+2]))
                    cp = cp2
                    cunnetLines = len(cp)-2

                return self.GetPoint(t, cp[0], cp[1], cp[2])

    def CurveHelf(self, t):
        if len(self.points) == 2:
            return Vector3.Lerp(self.points[0], self.points[1], t)
        elif len(self.points) == 3:
            return self.GetPoint(t, self.points[0], self.points[1], self.points[2])
        else: # N차 베지어 곡선
            return self.GetCurvePointHelf(t)

    def CreateCurveHelf(self, count):
        for i in range(count):
            self.curvePoint.append(self.CurveHelf(i/count))

    def Closed(self):
        self.points.append(self.points[0])

#----------------------------------------------------------------------------------------------------------------

class BezierHandle2D():
    points = []
    linePoints = []
    # closed = False

    def __init__(self):
        pass
    def __del__(self):
        pass

    def AddPoint(self, vector3):
        self.points.append(vector3)

    def Points(self):
        return self.points

    # 코드 분석 해야 됨
    # def GetPoint(self, t, vt2p0, vt2p1, vt2p2, vt2p3):
    #     cx = 3 * (vt2p1.X - vt2p0.X)
    #     cy = 3 * (vt2p1.Y - vt2p0.Y)
    #     bx = 3 * (vt2p2.X - vt2p1.X) - cx
    #     by = 3 * (vt2p2.Y - vt2p1.Y) - cy
    #     ax = vt2p3.X - vt2p0.X - cx - bx
    #     ay = vt2p3.Y - vt2p0.Y - cy - by
    #     Cube = t * t * t
    #     Square = t * t

    #     resX = (ax * Cube) + (bx * Square) + (cx * t) + vt2p0.X
    #     resY = (ay * Cube) + (by * Square) + (cy * t) + vt2p0.Y

    #     return Vector2(resX, resY)

    # def Curve(self, count, vt2p0, vt2p1, vt2p2, vt2p3):
    #     for t in range(count):
    #         PlotPoint = self.GetPoint(t, vt2p0, vt2p1, vt2p2, vt2p3)
    #     pass

#----------------------------------------------------------------------------------------------------------------  

class BezierHandle3D():
    points = []
    linePoints = []
    # closed = False

    def __init__(self):
        pass
    def __del__(self):
        pass

    def AddPoint(self, vector2):
        self.points.append(vector2)

    def GetPoints(self):
        return self.points

#----------------------------------------------------------------------------------------------------------------  

# win = Tk()
# win.title("Bezier")
# win.geometry("1580x1080")

# can = Canvas(win, height = 1080, width = 1580)
# can.pack()

# cur2d = BezierCurve2D()
# cur2d.AddPoint((50, 380))
# cur2d.AddPoint((180, 170))
# cur2d.AddPoint((310, 430))
# cur2d.AddPoint((450, 160))
# cur2d.AddPoint((580, 410))
# cur2d.AddPoint((680, 160))
# # cur2d.AddPoint((780, 460))

# can.create_oval(45, 375, 55, 385, fill = "pink")
# can.create_oval(175, 165, 185, 175, fill = "pink")
# can.create_oval(305, 425, 315, 435, fill = "pink")
# can.create_oval(445, 155, 455, 165, fill = "pink")
# can.create_oval(575, 405, 585, 415, fill = "pink")
# can.create_oval(675, 155, 685, 165, fill = "pink")
# can.create_oval(775, 455, 785, 465, fill = "pink")

# count = 100
# for i in range(count):
#     curvePoint = cur2d.Curve(i/count)
#     can.create_oval(curvePoint[0]-1, curvePoint[1]-1, curvePoint[0]+1, curvePoint[1]+1, fill = "black")

# win.mainloop()