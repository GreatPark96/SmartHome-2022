import threading
from bluetooth import *
import sys

socket = BluetoothSocket(RFCOMM)

#socket.connect((sys.argv[1], 1)) # 대상 디바이스의 맥주소를 실행시 인자값으로 받음

mac_add = "98:DA:D0:00:56:A2"

try:
    socket.connect((mac_add, 1)) # 대상 디바이스 맥주소 입력
except:
    print("Con't Connect Bluetooth Pair.")
    socket.close(s)
    exit()

print("Bluetooth connected!")

# Arduino to Python  Data 수신 함수
def data_receive():
    while True:
        data = socket.recv(1024)
        decode_data = data.decode() # 문자열 형태임
        decode_data = decode_data.strip() # 문자열 끝 개행제거 
        
        if (decode_data.isdigit()==True):
            result = int(decode_data)
        else:
            result = decode_data
            
        print(result)

# Python to Arduino Data 송신 함수 
def data_send():
    msg = input("send message : ")
    socket.send(msg)


# 메세지를 받는 쓰레드 생성
receive_t = threading.Thread(target=data_receive, args=())
receive_t.start()


while True:
    data_send()
    
socket.close()
