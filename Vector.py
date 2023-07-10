# 파이선구현 참조
# https://junstar92.tistory.com/357
# https://blockdmask.tistory.com/522
# https://www.programcreek.com/python/?CodeExample=normalize+vector 노말라이즈 구현 예제
# https://mole-starseeker.tistory.com/31 노말라이즈 개념 Z-Score Normalization 로 구현 해야 됨 (X – 평균) / (표준편차)
# https://ko.khanacademy.org/math/statistics-probability/summarizing-quantitative-data/variance-standard-deviation-sample/a/population-and-sample-standard-deviation-review 표준편차 예제
# https://www.programcreek.com/python/?CodeExample=look+at 룩앳 예제

import math
# from math import dist

#----------------------------------------------------------------------------------------------------------------

class Vector1:
    
    @classmethod
    def Lerp(self, startPos, endPos, t):
        return (startPos * (1.0 - t) + endPos * t)

#----------------------------------------------------------------------------------------------------------------

class Vector2:
    x = 0.0
    y = 0.0
    
    position = (x, y)

    zero = (0.0, 0.0)
    one = (1.0, 1.0)
    left = (-1.0, 0.0)
    right = (1.0, 0.0)
    up = (0.0, 1.0)
    down = (0.0, -1.0)

    def __init__(self):
        pass

    def __del__(self):
        pass

    @classmethod
    def Abs(self, vt2):
        return (abs(vt2[0]), abs(vt2[1]))

    @classmethod
    def Add(self, vt1, vt2):
        return ((vt1[0] + vt2[0]), (vt1[1] + vt2[1]))

    @classmethod
    def Sub(self, vt1, vt2):
        return ((vt1[0] - vt2[0]), (vt1[1] - vt2[1]))

    @classmethod
    def Truediv(self, vt1, vt2):
        return ((vt1[0] / vt2[0]), (vt1[1] / vt2[1]))

    @classmethod
    def Mod(self, vt1, vt2):
        return ((vt1[0] % vt2[0]), (vt1[1] % vt2[1]))
        
    @classmethod
    def Mul(self, vt1, vt2):
        return ((vt1[0] * vt2[0]), (vt1[1] * vt2[1]))
    
    @classmethod
    def Lerp(self, startPos, endPos, t):
        return (startPos[0] * (1.0 - t)+ endPos[0] * t, startPos[1] * (1.0 - t)+ endPos[1] * t)

    @classmethod
    def Distance(self, vt1, vt2):
        a = vt2[0] - vt1[0]
        b = vt2[1] - vt1[1]
        return math.sqrt((a * a) + (b * b))

    @classmethod
    def Dot(self, vt1, vt2):
        return sum([i*j for (i, j) in zip(vt1, vt2)])

    @classmethod
    def Normalize(self, vt2):
        return (((vt2[0] - 0.0) / self.Sdt(vt2)) * 0.5, ((vt2[1] - 0.0) / self.Sdt(vt2)) * 0.5)

    def Sdt(lst):
        sdt = ave = 0
        for i in range(len(lst)): ave = ave + lst[i]
        for d in range(len(lst)): sdt = sdt + math.pow((lst[d] - ave),2)
        sdt = sdt / len(lst)

        return math.sqrt(sdt)

    def Min(self):
        return min(self.position)

    def Max(self):
        return max(self.position)

    def Lookat(self, target):
        pass
    
    def Call2(self):
        print("aaaa");

#----------------------------------------------------------------------------------------------------------------

class Vector3:
    x = 0.0
    y = 0.0
    z = 0.0

    position = (x, y, z)

    zero = (0.0, 0.0, 0.0)
    one = (1.0, 1.0, 1.0)
    left = (-1.0, 0.0, 0.0)
    right = (1.0, 0.0, 0.0)
    forward = (0.0, 1.0, 0.0)
    back = (0.0, -1.0, 0.0)
    top = (0.0, 0.0, 1.0)
    bottom = (0.0, 0.0, -1.0)

    def __init__(self):
        pass

    def __del__(self):
        pass

    @classmethod
    def Abs(self, vt3):
        return (abs(vt3[0]), abs(vt3[1]), abs(vt3[2]))

    @classmethod
    def Add(self, vt1, vt2):
        return ((vt1[0] + vt2[0]), (vt1[1] + vt2[1]), (vt1[2] + vt2[2]))

    @classmethod
    def Sub(self, vt1, vt2):
        return ((vt1[0] - vt2[0]), (vt1[1] - vt2[1]), (vt1[2] - vt2[2]))

    @classmethod
    def Truediv(self, vt1, vt2):
        return ((vt1[0] / vt2[0]), (vt1[1] / vt2[1]), (vt1[2] / vt2[2]))

    @classmethod
    def Mod(self, vt1, vt2):
        return ((vt1[0] % vt2[0]), (vt1[1] % vt2[1]), (vt1[2] % vt2[2]))
        
    @classmethod
    def Mul(self, vt1, vt2):
        return ((vt1[0] * vt2[0]), (vt1[1] * vt2[1]), (vt1[2] * vt2[2]))
    
    @classmethod
    def Lerp(self, startPos, endPos, t):
        
        return (startPos[0] *  (1.0 - t)+ endPos[0] * t, startPos[1] *  (1.0 - t)+ endPos[1] * t, startPos[2] *  (1.0 - t)+ endPos[2] * t)

    @classmethod
    def Distance(self, vt1, vt2):
        a = vt2[0] - vt1[0]
        b = vt2[1] - vt1[1]
        c = vt2[2] - vt1[2]
        return math.sqrt((a * a) + (b * b) + (c * c))

    @classmethod
    def Dir(self, stPoint, endPoint):
        return self.Normalize((endPoint[0]-stPoint[0], endPoint[1]-stPoint[1], endPoint[2]-stPoint[2]))
    
    @classmethod
    def Dot(self, vt1, vt2):
        return sum([i*j for (i, j) in zip(vt1, vt2)])

    @classmethod
    # Y 축이 Up 일때
    def Lookat2(self, vt1, vt2):
        rtX = math.atan2(vt2[1], vt1[2])
        rtY = math.atan2(vt2[0], vt1[2])
        rtZ = math.atan2(vt2[1], vt1[0])
        
        degreeX = rtX * 180 / math.pi
        degreeY = rtY * 180 / math.pi
        degreeZ = rtZ * 180 / math.pi
        
        return (degreeX, degreeY, degreeZ)
        # return (rtX, rtY, rtZ)
    
    @classmethod
    def Lookat(sel  = vt2[0] - vt1[0]
        rtY = vt2[1] - vt1[1]
        rtZ = vt2[2] - vt1[2]
        length = math.sqrt(rtX * rtX + rtY * rtY + rtZ * rtZ)

        pitch = 0.0
        roll = 0.0
        yaw = 0.0
        
        pitch = math.asin(rtY / length)
        yaw = math.atan2(-rtX, -rtZ)
        
        if vt1[0] < vt2 [0]:
            pass
        else:
            pitch = pitch * -1.0
        
        if vt1[1] < vt2[1]:
            pass
        else:
            yaw = yaw * -1.0

        return (pitch, roll, yaw)
    
    # def SelfNormal(self, vt3):
    #     return (((vt3[0] - 0.0) / self.Sdt(vt3)) * 0.666, ((vt3[1] - 0.0) / self.Sdt(vt3)) * 0.666, ((vt3[2] - 0.0) / self.Sdt(vt3)) * 0.666)

    @classmethod
    def Normalize(self, vt3):
        return (((vt3[0] - 0.0) / self.Sdt(vt3)) * 0.666, ((vt3[1] - 0.0) / self.Sdt(vt3)) * 0.666, ((vt3[2] - 0.0) / self.Sdt(vt3)) * 0.666)

    def Sdt(lst):
        sdt = ave = 0
        for i in range(len(lst)): ave = ave + lst[i]
        for d in range(len(lst)): sdt = sdt + math.pow((lst[d] - ave),2)
        sdt = sdt / len(lst)

        return math.sqrt(sdt)

    def Min(self):
        return min(self.position)

    def Max(self):
        return max(self.position)

#----------------------------------------------------------------------------------------------------------------

class Vector4:
    x = 0.0
    y = 0.0
    z = 0.0
    w = 0.0

    position = (x, y, z, w)

    zero = (0.0, 0.0, 0.0, 0.0)
    one = (1.0, 1.0, 1.0, 1.0)

    def __init__(self):
        pass

    def __del__(self):
        pass

    @classmethod
    def Abs(self, vt4):
        return (abs(vt4[0]), abs(vt4[1]), abs(vt4[2]), abs(vt4[2]))

    @classmethod
    def Add(self, vt1, vt2):
        return ((vt1[0] + vt2[0]), (vt1[1] + vt2[1]), (vt1[2] + vt2[2]), (vt1[3] + vt2[3]))

    @classmethod
    def Sub(self, vt1, vt2):
        return ((vt1[0] - vt2[0]), (vt1[1] - vt2[1]), (vt1[2] - vt2[2]), (vt1[3] - vt2[3]))

    @classmethod
    def Truediv(self, vt1, vt2):
        return ((vt1[0] / vt2[0]), (vt1[1] / vt2[1]), (vt1[2] / vt2[2]), (vt1[3] / vt2[3]))

    @classmethod
    def Mod(self, vt1, vt2):
        return ((vt1[0] % vt2[0]), (vt1[1] % vt2[1]), (vt1[2] % vt2[2]), (vt1[3] % vt2[3]))
        
    @classmethod
    def Mul(self, vt1, vt2):
        return ((vt1[0] * vt2[0]), (vt1[1] * vt2[1]), (vt1[2] * vt2[2]), (vt1[3] * vt2[3]))
    
    @classmethod
    def Lerp(self, startPos, endPos, t):
        return (startPos[0] *  (1.0 - t)+ endPos[0] * t, startPos[1] *  (1.0 - t)+ endPos[1] * t, startPos[2] *  (1.0 - t)+ endPos[2] * t, startPos[3] *  (1.0 - t)+ endPos[3] * t)

    @classmethod
    def Distance(self, vt1, vt2):
        a = vt2[0] - vt1[0]
        b = vt2[1] - vt1[1]
        c = vt2[2] - vt1[2]
        d = vt2[3] - vt1[3]
        return math.sqrt((a * a) + (b * b) + (c * c) + (d * d))

    @classmethod
    def Dot(self, vt1, vt2):
        return sum([i*j for (i, j) in zip(vt1, vt2)])

    @classmethod
    def Normalize(self, vt4):
        return (((vt4[0] - 0.0) / self.Sdt(vt4)) * 0.75, ((vt4[1] - 0.0) / self.Sdt(vt4)) * 0.75, ((vt4[2] - 0.0) / self.Sdt(vt4)) * 0.75, ((vt4[2] - 0.0) / self.Sdt(vt4)) * 0.75)

    def Sdt(lst):
        sdt = ave = 0
        for i in range(len(lst)): ave = ave + lst[i]
        for d in range(len(lst)): sdt = sdt + math.pow((lst[d] - ave),2)
        sdt = sdt / len(lst)

        return math.sqrt(sdt)

    def Min(self):
        return min(self.position)

    def Max(self):
        return max(self.position)

#----------------------------------------------------------------------------------------------------------------


# CurveList = Vector4().position = (1.0, 1.0, 1.0, 1.0)
# toPath = Vector4().position = (1.0, 0.0, 0.0, 0.0)
# setdir = Vector2().position = (-2.0, -1.0)

# print(Vector3.Dot(CurveList, toPath))
# print(Vector4.Distance(CurveList, toPath))
# print(Vector4.Normalize(CurveList))
# print(Vector2.Abs(CurveList))
# print(Vector2.Add(CurveList,toPath))
# print(Vector2.Lerp((1.0,1.0),(2.0,2.0),0.5))


# aaa = (0, 0, 0)
# bbb = (-1.4, -2.9, -5)
# ccc = Vector3.Lookat2(aaa, bbb)
# print(ccc)