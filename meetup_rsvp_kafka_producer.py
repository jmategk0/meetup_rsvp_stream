import asyncio
import websockets
import json
from kafka import KafkaProducer
from utils import clean_meetup_result
# from pprint import pprint

meet_up_stream = "ws://stream.meetup.com/2/rsvps"
topic_name = "meetup_rsvp"
kafka_server = "localhost:2181"

producer = KafkaProducer(
    bootstrap_servers=kafka_server,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

async def get_meetup_rsvps():
    async with websockets.connect(meet_up_stream) as websocket:
        while True:
            meetup_rsvp = await websocket.recv()
            data = json.loads(meetup_rsvp)
            clean_data = clean_meetup_result(data)
            producer.send(topic_name, clean_data)
            # pprint(clean_data)


asyncio.get_event_loop().run_until_complete(get_meetup_rsvps())
