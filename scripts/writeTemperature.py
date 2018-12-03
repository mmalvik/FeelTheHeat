from influxdb import InfluxDBClient

print("Starting registration...")
databaseName = 'Temperatures'

client = InfluxDBClient(host='localhost', port=8086, database=databaseName)
client.create_database(databaseName)

json_body = [
    {
        "measurement": "Temperature",
        "tags": {
            "sensor": "DHT_22",
        },
        "fields": {
            "temperature": 15
        }
    },
    {
        "measurement": "Temperature",
        "tags": {
            "sensor": "DS18B20",
        },
        "fields": {
            "temperature": 16
        }
    }
]

print(client.write_points(json_body))

print("Registration complete...")