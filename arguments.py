# vrAEBase = 0
# class TestSpawn(vrAEBase):
#     print('A')
#     def __init__(self, setName):
#         print('B')
#         vrAEBase.__init__(self)
#         print(setName)
#
# print("live")
# ta = []
#
# ta.append(TestSpawn("1234"))
# print(list.ta)

#원하는 print 출력
#live
#A
#B
#setName
#list.ta 배열

class TestSpawn :
    def __init__(self, setName): #self = 만들어질 객체, setName = 들어올 인수
        print('A')
        print('B')
        self.setName = setName # 만들어질 객체에 인수를 저장
        print(self.setName)

a = TestSpawn("1234") #TestSpawn 클래스에서 '1234'를 setName에 저장한 a 객체를 생성
print('live')
ta = [1,2,3] # 1,2,3 인자를 가진 리스트 ta 를 만듬
ta.pop(0) # indexNum 0 을 가진 엘레멘트 제거.
ta.append(a.setName + str( 1153) + '최강삼성') # ta list에 a의 setName = '1234' 를 인자로 추가
print(ta) # 리스트 인자 출력
