# 예외처리하고 클래스로 구현 가능하면 클래스로 구현
import threading
from bluetooth import *
import sys

socket = BluetoothSocket(RFCOMM)

#socket.connect((sys.argv[1], 1)) # 대상 디바이스의 맥주소를 실행시 인자값으로 받음

socket.connect(("98:DA:D0:00:56:A2", 1)) # 대상 디바이스 맥주소 입력

print("bluetooth connected!")


def data_receive():
    while True:
        data = socket.recv(1024)
        park = data.decode() # 문자열 형태임
        int(park)
        print(park)

def data_send():
    msg = input("send message : ")
    socket.send(msg)
'''   
# 메세지를 보내는 쓰레드
send_t = threading.Thread(target=data_send, args=())
send_t.start()
'''

# 메세지를 받는 쓰레드
receive_t = threading.Thread(target=data_receive, args=())
receive_t.start()


while True:
    data_send()
    
socket.close()
888
