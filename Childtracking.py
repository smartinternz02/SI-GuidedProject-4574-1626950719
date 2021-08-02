import json
import wiotp.sdk.device
import time

myConfig = {
    "identity": {
        "orgId": "q2mp6a",
        "typeId": "HarishDevice",
        "deviceId": "22072002"
    },
    "auth": {
        "token": "123456789"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
    name= "Harish"
    #in area location

    latitude= 11.0168
    longitude= 76.9558

    #out area location

    #latitude= 11.0170
    #longitude= 76.9600
    myData={'name': name, 'lat':latitude,'lon':longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
    print("Data published to IBM IoT platform: ",myData)
    time.sleep(5)

client.disconnect()
    
    
    
