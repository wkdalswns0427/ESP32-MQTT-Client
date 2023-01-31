# ESP32-MQTT-Client
API server, Frontend, and Frimware to manipulate multi esps via web

## Configuration
- MCU : ESP32 -> LOLIN D32 PRO
- API server : REST API based on FastAPI framework
- Frontend : 

## How to Use
### MCU(ESP32)
upload the ```.ino``` file using Arduino IDE

### API server
run code below
```
uvicorn app:app --host 0.0.0.0 --reload
```

### Frontend
