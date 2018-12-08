import json
import datetime
from influxdb import InfluxDBClient
from ReadTemperatures import read_ds18b20_temp, read_dht22

def read_config():
    with open('dbconfig.json') as f:
        data = json.load(f)
        databaseName = data["databaseName"]
        databaseUserName = data["databaseUserName"]
        databasePassword = data["databasePassword"]
    return (databaseName, databaseUserName, databasePassword)

def utc_now_seconds():
    now = datetime.datetime.utcnow()
    return int(now.strftime("%s"))

def create_influx_json():
    timestamp = utc_now_seconds()
    humidity,temperature = read_dht22()
    return [
        {
            "measurement": "IndoorClimate",
            "tags": {
                "sensor": "DHT_22",
            },
            "time": timestamp,
            "fields": {
                "temperature": temperature,
                "humidity": humidity
            }
        },
        {
            "measurement": "IndoorClimate",
            "tags": {
                "sensor": "DS18B20",
            },
            "time": timestamp,
            "fields": {
                "temperature": read_ds18b20_temp()
            }
        }
    ]    

print("Starting registration...")

db, u, p = read_config()
print(db, u, p)

client = InfluxDBClient(host='40.87.130.203', port=8086, database=db, username=u, password=p)
client.create_database(db)

print(create_influx_json())

try:
    client.write_points(create_influx_json(), time_precision='s')
except:
    print("Writing to DB failed!")

print("Registration complete...")