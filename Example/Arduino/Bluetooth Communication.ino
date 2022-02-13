/*
****************************************************************************
  @ Name: Bluetooth Communication.ino
  @ Author: J.H
  @ Date: 2022. 02. 01.
  @ Update: None
  @ Comment: Arduino - Raspberry PI 간 블루투스 통신.
*****************************************************************************
*/



#include <SoftwareSerial.h>
 
int RX=7; // 아두이노 디지털 7번 핀과 BT 모듈 TX 연결
int TX=8; // 아두이노 디지털 8번 핀과 BT 모듈 RX 연결

SoftwareSerial bluetooth(RX, TX);

void setup(){
  Serial.begin(9600);
  bluetooth.begin(9600);
}
 
void loop(){
  
  if (bluetooth.available()) // 블루투스 시리얼에서 읽을 수 있는 바이트의 수가 0이 아니면
  {
    Serial.write(bluetooth.read());
  }
  if (Serial.available()) // 아두이노 시리얼에서 읽을 수 있는 바이트의 수가 0이 아니면
  {
    bluetooth.write(Serial.read()); 
  }
}
