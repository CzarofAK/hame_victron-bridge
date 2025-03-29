from homeassistant.components import mqtt as hamqtt
from homeassistant.components.mqtt import async_publish
import json
import copy

mqtt_host = "venus.local" #or IP, if no DNS available
mqtt_port = 1883

clientid = "hameservice"
portalId = ""

registration = {
    "clientId": clientid,
    "connected": 1,
    "version": "v0.1",
    "services": {
        "Diesel": "tank", #Type of sensor see https://github.com/freakent/dbus-mqtt-devices
        "AdBlue": "tank"
    }
}

unregister = copy.deepcopy(registration)
unregister["connected"] = 0

# "Remaining": 0.5678,
dataDiesel = {
    "Level": 12.34,
    "deviceId" : ""
}

dataAdBlue = {
    "Level": 0,
    "deviceId" : ""
}

def writeValue(portalId, deviceId, key, value):
    topic = "W/{}/tank/{}/{}".format(portalId, deviceId, key)
    log.debug("{} = {}".format(topic, value ) )
    hass.components.mqtt.publish(hass, topic, json.dumps({ "value": value }))

#Trigger at loading of the script
@time_trigger
def run_on_startup_or_reload():
    log.info("hameservice is loaded")
    hass.components.mqtt.publish(hass, "device/{}/Status".format(clientid), json.dumps(unregister))
    hass.components.mqtt.publish(hass, "device/{}/Status".format(clientid), json.dumps(registration))
    dataDiesel["Level"] = state.get("sensor.tbd_fuel_level")
    dataAdBlue["Level"] = state.get("sensor.tbd_adblue_level")

@time_trigger('period(now + 1m, 1m)')
def on_time_trigger():
    log.info("timmer called")
    writeValue(portalId, dataDiesel["deviceId"], "Level", dataDiesel.get("Level"))

@mqtt_trigger("device/hameservice/DBus")
def on_message_dbus(payload, topic):
    log.debug("Dbus payload " + str(payload))
    global portalId
    dbus_msg = json.loads(payload)
    portalId = dbus_msg.get("portalId")
    dataDiesel["deviceId"] = dbus_msg.get("deviceInstance").get("Diesel")
    writeValue(portalId, dataDiesel["deviceId"], "Level", dataDiesel.get("Level"))
    dataAdBlue["deviceId"] = dbus_msg.get("deviceInstance").get("AdBlue")
    writeValue(portalId, dataAdBlue["deviceId"], "Level", dataAdBlue.get("Level"))

@mqtt_trigger("simuvalue/hameservice/#")
def on_message_simu(payload, topic):
    log.debug("simu payload " + payload)

    log.debug("simu " + topic + " payload "+ str(payload))
    global portalId

    dbus_msg = json.loads(payload)
    # Todo make it better beginer Code...
    if(topic == "simuvalue/hameservice/Diesel"):
        dataDiesel["Level"] = dbus_msg.get("Level")

    if(dataDiesel["deviceId"] == ""):
        print("error missing Diesel device id")
    else:
        writeValue(portalId, dataDiesel["deviceId"], "Level", dataDiesel.get("Level"))

@service
def testCerbo(action=None, id=None):
    """yaml
name: testCerbo
description: Cerbo Init Test.
fields:
    action:
        description: turn_on turns on the light, fire fires an event
        example: "{ 'Level': 12.5 }"
        required: true
"""
    log.info("testCerbo " + action)
    async_publish(hass, "simuvalue/hameservice/Diesel", action)

@state_trigger("sensor.tbd_fuel_level")
def tbd_fuel_change(value=None):
    log.info("tbd_fuel_change " + value)
    dataDiesel["Level"] = value
    writeValue(portalId, dataDiesel["deviceId"], "Level", dataDiesel.get("Level"))

@state_trigger("sensor.tbd_adblue_level")
def tbd_adblue_change(value=None):
    log.info("tbd_adblue_level " + value)
    dataAdBlue["Level"] = value
    writeValue(portalId, dataAdBlue["deviceId"], "Level", dataAdBlue.get("Level"))
