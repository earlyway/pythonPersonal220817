

animals = ["사자", "호랑이"]

name = animals[0]



'''
list 데이터 추가하기 list.append(추가할 데이터)

list 데이터 삭제하기 del listname[삭제할 데이터의 index Number]

list 슬라이싱 분리.   listname[시작할 index number:끝 index number+1]

list 길이. len(listname)

list정렬. listname.sort() 오름차순 정렬

'''

animals.append("하마")
animals.append(1)


del animals[-1] #-1은 마지막 데이터를 삭제.


slice = animals[0:2]


length = len(animals)

animals.sort()
#animals.sort(reverse=True) 로 하게되면 내림차순으로 정렬됨.





print(animals)
print(slice)
print(length)