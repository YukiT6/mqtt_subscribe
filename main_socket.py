import paho.mqtt.client as mqtt
import socket
import time

MQTT_PORT = 1883
KEEP_ALIVE = 60
HOST = "150.65.230.91"
PORT = 3361

TOPIC = "sensor/co2/SCD30_01"

#Brokerに接続できたとき


def on_connect(client, userdata, flag, rc):
  print("connect broker:" + str(rc))
  client.subscribe(TOPIC)

#Brokerと切断したとき


def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
    print("disconnect broker")

#メッセージ受信


def on_message(client, userdata, msg):
  print("Data = " + str(msg.payload.decode()))
  if(int(msg.payload.decode()) == 0):
    print("sensor data missing...")
  elif (int(msg.payload.decode()) >= 900):
    print("high")
    send_socket(0)
  elif (int(msg.payload.decode()) < 900):
    print("Low")
    send_socket(1)


def send_socket(num):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((HOST, PORT))
  s.settimeout(2)
  if (num == 0):
    print("Light ON\n")
    sendline = b"150.65.230.114:029000:0x80,0x30\n"
  elif(num == 1):
    print("Light OFF\n")
    sendline = b"150.65.230.114:029000:0x80,0x31\n"
  s.sendall(sendline)
  s.close()



client = mqtt.Client()

  #コールバックを登録
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)

  #待ち受け
client.loop_forever()
