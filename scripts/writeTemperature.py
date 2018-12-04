from influxdb import InfluxDBClient

print("Starting registration...")
databaseName = 'FeelTheHeat'

client = InfluxDBClient(host='localhost', port=8086, database=databaseName)
client.create_database(databaseName)

def funcname():
    return 18


json_body = [
    {
        "measurement": "IndoorClimate",
        "tags": {
            "sensor": "DHT_22",
        },
        "fields": {
            "temperature": funcname(),
            "humidity": 38
        }
    },
    {
        "measurement": "IndoorClimate",
        "tags": {
            "sensor": "DS18B20",
        },
        "fields": {
            "temperature": 24
        }
    }
]

print(client.write_points(json_body))

print("Registration complete...")