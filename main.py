import paho.mqtt.client as mqtt
import pexpect

MQTT_PORT = 1883
KEEP_ALIVE = 60
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
    pub("150.65.230.91", "0")
  elif (int(msg.payload.decode()) < 900):
    print("Low")
    pub("150.65.230.91", "1")


def pub(ipaddr, num):
    child = pexpect.spawn("telnet " + ipaddr + " 3361")
    while (True):
        if (num == "0"):
            child.sendline("150.65.230.114:029000:0x80,0x30")
            child.expect("OK,150.65.230.114:029003:0x80")
            break
        elif (num == "1"):
            child.sendline("150.65.230.114:029000:0x80,0x31")
            child.expect("OK,150.65.230.114:029003:0x80")
            num = 10
            break

client = mqtt.Client()

  #コールバックを登録
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)

  #待ち受け
client.loop_forever()
