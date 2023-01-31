import uvicorn
import paho.mqtt.client as mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
mqtt_config = MQTTConfig()
fast_mqtt = FastMQTT(config=mqtt_config)
fast_mqtt.init_app(app)

broker = 'localhost'
pubclient = mqtt.Client("pubclient")
pubclient.connect(broker,1883)

class Item(BaseModel):
    name : str
    number : int
    content : str

def mqttclient():
    pubclient = mqtt.Client("pubclient")
    pubclient.connect('localhost',1883)
    pubclient.publish("esp/test", "atest message")

def fastmqttCLient(num):
    topic = "esp/" + num
    fast_mqtt.publish(topic, "publisher")


@app.get("/")
async def first():
    hi = "hello"
    return hi

@app.get("/publish")
async def pub():
    fast_mqtt.publish("esp/1", "publisher")
    ret = "esp/test : atest message"
    return ret

@app.post("/command")
async def unaposta(item : Item):
    topic = item.name + "/" + str(item.number)
    fast_mqtt.publish(topic, item.content)
    return topic
