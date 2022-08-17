import time


a = 0

while a < 4:

    a = a + 1
    print(a)
    time.sleep(4)
    if a == 3:
        print('라스트')
        break
    
