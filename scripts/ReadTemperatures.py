import Adafruit_DHT as dht
import os
import glob
import datetime

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

deviceFolder = "/sys/bus/w1/devices/28-000009fe71d2"
deviceFile = deviceFolder + "/w1_slave"

def read_ds18b20_raw():
    file = open(deviceFile, "r")
    lines = file.readlines()
    file.close()
    return lines

def read_ds18b20_temp():
    lines = read_ds18b20_raw()
    if "YES" not in lines[0]:
        return 999
    equalsSignPos = lines[1].find("t=")
    if equalsSignPos == -1:
        return 666
    temp = lines[1][equalsSignPos+2:]
    temperature = float(temp) / 1000.0
    return temperature

def read_DHT22():
    sensorHumidity,sensorTemperature = dht.read_retry(dht.DHT22, 23)
    humidity = round(sensorHumidity, 3)
    temperature = round(sensorTemperature, 3)
    return (humidity, temperature)

def UtcNowSeconds():
    now = datetime.datetime.utcnow()
    return int(now.strftime("%s"))

print(UtcNowSeconds())
print("DHT22 data:")
print(read_DHT22())
print("DS temp:")
print(read_ds18b20_temp())
