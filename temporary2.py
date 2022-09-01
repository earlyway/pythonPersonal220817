
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

import time
class Action():
    count = 0
    lastFrameTime = 0
    createTime = 0
    #my = 0

    def __init__(self):
        self.addLoop()


    def loop(self):
        self.currentTime = time.time()
        self.deltaTime = self.currentTime - self.lastFrameTime
        self.createTime += self.deltaTime

        while self.my == 0 :
            self.count = self.count + 0.05
            self.my += self.count

            if self.my == 1 :
                self.subLoop()
                break




#------------
my = findMaterial.getTransparency("VredAlpha")

aaa = Action()
#aaa = findMaterial("VredAlpha")
aaa.loop(my)
print(dir(aaa))
#aaa.setTransparency(0.0)


