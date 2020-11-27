# publisher

import time
import paho.mqtt.client as mqtt
import circuit # 초음파 센서 입력 모듈 임포트
import myCamera 

flag = False # True
tag1 = 0

def on_connect(client, userdata, flag, rc):
        client.subscribe("led", qos = 0)
        client.subscribe("facerecognition", qos = 0)
        
def on_message(client, userdata, msg) :
        global flag
        global tag1
        command = msg.payload.decode("utf-8")
        if command == "action":
            print("action msg received..")
            flag = True
        else:
            msg = int(msg.payload);
            print(msg)
            tag1 = 2
            circuit.controlLED(msg)# msg는 0 또는 1의 정수
            if msg == 0:
                circuit.ledOnOff(msg)
                tag1 = 1
                

broker_ip = "localhost" # 현재 이 컴퓨터를 브로커로 설정

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker_ip, 1883)
client.loop_start()

while(True):
    if flag==True : # "action" 메시지 수신. 사진 촬영
        imageFileName = myCamera.takePicture() # 카메라 사진 촬영
        print(imageFileName)
        client.publish("image", imageFileName, qos=0)
        flag = False
        
    if tag1==1 : # "action" 메시지 수신. 사진 촬영
        timeset = time.time() # 카메라 사진 촬영
        tm = time.localtime(timeset)
        desktime = "퇴실 : %d-%d-%d %d:%d:%d" % (tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)
        client.publish("deskcheck", desktime, qos=0)
        tag1=0
        
    if tag1 == 2:
        timeset = time.time() # 카메라 사진 촬영
        tm = time.localtime(timeset)
        desktime = "입실 : %d-%d-%d %d:%d:%d"% (tm.tm_year,tm.tm_mon,tm.tm_mday,tm.tm_hour,tm.tm_min,tm.tm_sec)
        client.publish("deskcheck", desktime, qos=0)
        tag1=0
        
    distance = circuit.measureDistance()
    client.publish("ultrasonic", distance, qos=0)
    time.sleep(1)

client.loop_stop()
client.disconnect()
