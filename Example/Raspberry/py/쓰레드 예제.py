import threading


def one():
    for i in range(10):
        print("1")
    print("one fun END")


def two():
    for i in range(10):
        print("2")
    print("two fun END")
    
thread1 = threading.Thread(target=one, args=()) #thread1 생성 (one fun 호출, 인자값은 없음)
thread1.start() # thread1 시작

thread2 = threading.Thread(target=two, args=())
thread2.start()
