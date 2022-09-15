from os import stat_result
import paho.mqtt.client as mqtt
import socket
import time

MQTT_PORT = 1883
KEEP_ALIVE = 60
HOST = "150.65.230.91"
PORT = 3361


TOPIC = [("sensor/co2/SCD30_01",0),("status/human_detection",0),("actuator/tans2/window00",0)]

flag = 0
state_flag = 0

#Brokerに接続できたとき


def on_connect_sub(client, userdata, flag, rc):
  print("connect broker:" + str(rc))
  client.subscribe(TOPIC)

def on_connect_pub(client, userdata, flag, rc):
  print("connect broker:" + str(rc))
  

#Brokerと切断したとき
def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
    print("disconnect broker")

#メッセージ受信

def on_message(client, userdata, msg):
  global flag , state_flag
  print("Data = " + str(msg.payload.decode()))
  if(msg.topic == "status/human_detection"):
    state_flag = 1
  elif(msg.topic == "status/human_detection"):
    state_flag = 0
  if(state_flag == 1 and msg.topic == "sensor/co2/SCD30_01"):

    if(int(msg.payload.decode()) == 0):
      print("sensor data missing...")

    elif (int(msg.payload.decode()) >= 900):
      if(flag == 0):
        print("high")
        flag= 1
        send_socket(0)

      elif (int(msg.payload.decode()) < 900):
        if(flag == 1):
          print("Low")
          flag = 0
          send_socket(1)

#publishが完了したとき
def on_publish(client, userdata, mid):
  print("publish Done")

#socket送信
def send_socket(num):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.settimeout(2)
  if (num == 0):
    print("Light ON\n")
    pub(num)
    sendline = b"150.65.230.114:029000:0x80,0x30\n"
  elif(num == 1):
    print("Light OFF\n")
    pub(num)
    sendline = b"150.65.230.114:029000:0x80,0x31\n"
  s.sendall(sendline)
  s.close()

def check():
    client = mqtt.Client()
    #コールバックを登録
    client.on_connect = on_connect_sub
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)

    #待ち受け
    client.loop_forever()


def pub(num):
    client = mqtt.Client()
    #コールバックを登録 
    client.on_connect = on_connect_pub
    client.on_disconnect = on_disconnect
    client.on_publish = on_publish

    client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)  
    if(num == 0):
      client.publish(TOPIC[2][0],"Open")
    else : 
      client.publish(TOPIC[2][0],"Close")


def main():
  client = mqtt.Client()
  #コールバックを登録
  client.on_connect = on_connect_sub
  client.on_disconnect = on_disconnect
  client.on_message = on_message

  client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)

  #待ち受け
  client.loop_forever()

if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
  main()    # メイン関数を呼び出す
