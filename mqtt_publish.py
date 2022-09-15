from time import sleep
import paho.mqtt.client as mqtt

MQTT_PORT = 1883
KEEP_ALIVE = 60

TOPIC = "status/human_detection"

#Brokerに接続できたとき
def on_connect(client, userdata, flag, rc):
  print("Connect Broker:" + str(rc))

#Brokerと切断したとき
def on_disconnect(client, userdata, flag, rc):
  if rc != 0:
     print("disconnect broker")

#publishが完了したとき
def on_publish(client, userdata, mid):
  print("publish Done")

def main():
  cnt = 0
  client = mqtt.Client()
  #コールバックを登録 
  client.on_connect = on_connect
  client.on_disconnect = on_disconnect
  client.on_publish = on_publish

  client.connect("150.65.179.250", MQTT_PORT, KEEP_ALIVE)  

  client.publish(TOPIC,"0")

  sleep(2)


if __name__ == '__main__':          # importされないときだけmain()を呼ぶ
  main()    # メイン関数を呼び出す