# python 블루투스 통신 예제

from bluetooth import *

socket = BluetoothSocket(RFCOMM) # 소켓 객체 생성

socket.connect(("98:DA:D0:00:56:A2", 1)) # 대상 맥주소 입력 및 1?(이건 알아보자)

print("bluetooth connected!")


def data_receive():
    while(1):
        data = socket.recv(1024) # 이것도 알아보자
        park = data.decode()#[:-2] # 받은 데이터 디코드 한다.
        
        
        print(int(park) + 1)
   


def data_send():
    
    msg = input("send message : ")
    socket.send(msg) # 입력 메세지 전달
    
    print ("ok !")
    



while True:
    
    data_receive()
    #send
    
    data_send()
    ##
    
    
    #if(park=="q"):
     #   print("Quit")
      #  break



    
socket.close()
