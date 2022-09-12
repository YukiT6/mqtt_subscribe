import paho.mqtt.client as mqtt 

MQTT_PORT = 1883
KEEP_ALIVE = 60
TOPIC = "sensor/co2/SCD30_01"

#Brokerに接続できたとき
def on_connect(client, userdata, flag, rc):
  print("connect broker:" + str(rc))
  client.subscribe(TOPIC) 

#Brokerと切断したとき
def on_disconnect(client, userdata, flag, rc):
  if  rc != 0:
    print("disconnect broker")

#メッセージ受信
def on_message(client, userdata, msg):
  print("Data = " + str(msg.payload.decode()))
  if(int(msg.payload.decode()) > 900):
    print("high")


client = mqtt.Client()  
#コールバックを登録     
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message

client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)

#待ち受け
client.loop_forever()
