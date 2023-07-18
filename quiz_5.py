'''
for 변수 in listname:
    명령블록
'''
for a in [1,2,3,4]:
    print(a)


'''
range(8)   0~7까지의 순서열을 반환
range(1,5) 1~4까지의 순서열을 반환
range(1,10,2) 1~9 사이에서 2씩 증가. 1,3,5,7,9 순서열로 반환
'''
for i in range(60):
    print(i+1, "분")

for a in range(1,13):
    print(a, "월")


'''
while  조건 :
    명령블록
'''
count = 0
while count <5:
    print(count, "번째 반복입니다")
    count = count + 1
    

#프로그램 사용자로부터 자연수를 입력받고 0부터 자연수까지의 합계를 출력하세요.
input_number = int(input("자연수를 입력하세요>>>"))
input_list = range(input_number+1)
print(input_list)

sum = 0
for i in input_list:
    sum = sum + i
print(sum)