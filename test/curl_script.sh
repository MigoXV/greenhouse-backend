# 上传传感器数据

curl -X 'POST' \
  'http://39.106.1.132:30002/data/upload/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "sensor_id": "sensor_01",
  "temperature": 22.5,
  "humidity": 45,
  "timestamp": "2024-03-25T15:00:00Z"
}'

# 查询传感器数据

curl -X 'GET' \
  'http://39.106.1.132:30002/data/query/?sensor_id=sensor_01' \
  -H 'accept: application/json'

curl -X 'GET' \
  'http://39.106.1.132:30002/data/query/?sensor_id=sensor_01&start=2024-03-25&end=2024-03-26' \
  -H 'accept: application/json'

# 注册设备
curl -X 'POST' \
  'http://39.106.1.132:30002/device/register/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "device_id": "esp8266_01",
  "location": "office",
  "sensors": ["temperature", "humidity"]
}'
