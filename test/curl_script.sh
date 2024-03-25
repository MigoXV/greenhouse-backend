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
