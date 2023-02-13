import uvicorn
import paho.mqtt.client as mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig
from fastapi import FastAPI
from utils.model import Item, DiscountItem, IsDiscount, DBItem
from utils.utils import dataHandler
from starlette.middleware.cors import CORSMiddleware
import httpx
import asyncio

app = FastAPI()
mqtt_config = MQTTConfig(host = "172.25.0.2", port=1883)
fast_mqtt = FastMQTT(config=mqtt_config)
fast_mqtt.init_app(app)

parking_api = "http://this_api_doesn_not_exist:8080"

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

async def call_parking_api(userInfo):
    async with httpx.AsyncClient() as Client:
        response = Client.get(parking_api, params=userInfo)
        data = response.json()
        return response
    return response


@app.get("/")
async def first():
    hi = "api server on"
    return hi

@app.get("/publish")
async def pub():
    fast_mqtt.publish("esp/1", "avalanche")
    ret = "esp/1 : avalanche"
    return ret


# -------------------- dummy api ---------------------
@app.post("/dummyon", description="dummy charger on")
async def dummyon(item : DiscountItem):

    dcItem = IsDiscount()
    datahandle = dataHandler()

    # decide whether to give discount or not
    if datahandle.matchCar(item.carnumber)==True:
        dcItem.discount = True

    topic = item.name + "/" + str(item.number)
    fast_mqtt.publish(topic, item.content)
    return dcItem

@app.post("/dummyoff")
async def dummyoff(item : Item):

    topic = item.name + "/" + str(item.number)
    fast_mqtt.publish(topic, item.content)

    # return topic+":"+item.content
    return True
# ----------------------------------------------------

# -------------------- actual api --------------------
# call_parking_api -> get yes or no data
@app.get("/chargerdiscountcheck")
async def chargerdiscountcheck(item : DiscountItem):

    dcItem = IsDiscount()
    

    # datahandle = dataHandler()

    # if datahandle.matchDate==True and datahandle.matchCar==True:
    #     dcItem.discount = True


    topic = item.name + "/" + str(item.number)
    fast_mqtt.publish(topic, item.content)

    return dcItem.discount

@app.post("/chargerbegin")
async def chargerbegin():

    return False