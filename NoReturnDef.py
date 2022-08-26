def sample(a,b):
    return print("%s,%s의 플러스값 : %s 마이너스값: %s" % (a,b,a+b, a-b))

print(sample(30,20))



#>>>출력
#30,20의 플러스값 : 50 마이너스값: 10
#None

#sample 이라는 함수의 구성요소중 하나인 print문이 수행되었을뿐 결과값은 없다.
#따라서 print문이 출력되고 다음줄에 None이 출력된 것을 볼 수 있다.
#왜냐하면 결과값은 오직 return 으로만 받을 수 있기 때문이다.
