from config import AppConfig
from sensors import Laser, Button
from MQTT import MQTT

if __name__ == '__main__':
    with AppConfig() as app_config:
        laser = Laser(7)
        button = Button(12)
        mqttclient = MQTT()
        while True:
            button.listen_onclick(laser.switch)
            message = 'Laser is ON' if laser.light_state else 'Laser is OFF'
            mqttclient.pulish(topic='signals/button', retain=True, payload=message)
