from homeassistant.components import mqtt as hamqtt
import json
import copy

mqtt_host = venus.local #or IP, if no DNS available
mqtt_port = 1883

clientid = hameservice
portalId = 

registration = {
    clientId clientid,
    connected 1,
    version v0.1,
    services {
        Diesel tank, #Type of sensor see httpsgithub.comfreakentdbus-mqtt-devices
        AdBlue tank
    }
}

unregister = copy.deepcopy(registration)
unregister[connected] = 0

# Remaining 0.5678,
dataDiesel = {
    Level 12.34,
    deviceId  
}

dataAdBlue = {
    Level 0,
    deviceId  
}

def writeValue(portalId, deviceId, key, value)
    topic = W{}tank{}{}.format(portalId, deviceId, key)
    log.debug({} = {}.format(topic, value ) )
    hass.components.mqtt.publish(hass, topic, json.dumps({ value value }))

#Trigger bei laden vom script
@time_trigger
def run_on_startup_or_reload()
    log.info(hameservice is loaded)
    hass.components.mqtt.publish(hass, device{}Status.format(clientid), json.dumps(unregister))
    hass.components.mqtt.publish(hass, device{}Status.format(clientid), json.dumps(registration))
    dataDiesel[Level] = state.get(sensor.fuel_level)
    dataAdBlue[Level] = state.get(sensor.adblue_level)


@mqtt_trigger(devicehameserviceDBus)
def on_message_dbus(payload, topic)
    log.debug(Dbus payload  + str(payload))
    global portalId
    dbus_msg = json.loads(payload)
    portalId = dbus_msg.get(portalId)
    dataDiesel[deviceId] = dbus_msg.get(deviceInstance).get(Diesel)
    writeValue(portalId, dataDiesel[deviceId], Level, dataDiesel.get(Level))
    dataAdBlue[deviceId] = dbus_msg.get(deviceInstance).get(AdBlue)
    writeValue(portalId, dataAdBlue[deviceId], Level, dataAdBlue.get(Level))

@mqtt_trigger(simuvaluehameservice#)
def on_message_simu(payload, topic)
    log.debug(simu payload  + payload)

    log.debug(simu  + topic +  payload + str(payload))
    global portalId

    dbus_msg = json.loads(payload)
    # Todo make it better beginer Code...
    if(topic == simuvaluehameserviceDiesel)
        dataDiesel[Level] = dbus_msg.get(Level)

    if(dataDiesel[deviceId] == )
        print(error missing Diesel device id)
    else
        writeValue(portalId, dataDiesel[deviceId], Level, dataDiesel.get(Level))

@service
def testCerbo(action=None, id=None)
    yaml
name testCerbo
description Cerbo Init Test.
fields
    action
        description turn_on turns on the light, fire fires an event
        example { 'Level' 12.5 }
        required true

    log.info(testCerbo  + action)
    hass.components.mqtt.publish(hass, simuvaluehameserviceDiesel, action)

@state_trigger(sensor.fuel_level)
def fuel_change(value=None)
    log.info(fuel_change  + value)
    dataDiesel[Level] = value
    writeValue(portalId, dataDiesel[deviceId], Level, dataDiesel.get(Level))

@state_trigger(sensor.adblue_level)
def adblue_change(value=None)
    log.info(adblue_level  + value)
    dataAdBlue[Level] = value
    writeValue(portalId, dataAdBlue[deviceId], Level, dataAdBlue.get(Level))
