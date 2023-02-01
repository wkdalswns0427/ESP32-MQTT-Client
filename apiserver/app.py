import uvicorn
import paho.mqtt.client as mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()
mqtt_config = MQTTConfig()
fast_mqtt = FastMQTT(config=mqtt_config)
fast_mqtt.init_app(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

class Item(BaseModel):
    name : str
    number : int
    content : str

@app.get("/")
async def first():
    hi = "api server on"
    return hi

@app.get("/publish")
async def pub():
    fast_mqtt.publish("esp/1", "avalanche")
    ret = "esp/1 : avalanche"
    return ret

@app.post("/command")
async def sendcommand(item : Item):
    topic = item.name + "/" + str(item.number)
    fast_mqtt.publish(topic, item.content)
    return topic

# --------------------- depricated ---------------------
# broker = 'localhost'
# pubclient = mqtt.Client("pubclient")
# pubclient.connect(broker,1883)

# def mqttclient():
#     pubclient = mqtt.Client("pubclient")
#     pubclient.connect('localhost',1883)
#     pubclient.publish("esp/test", "atest message")
# ------------------------------------------------------
