import asyncio
import websockets
import json
from pprint import pprint
from utils import clean_meetup_result

meet_up_stream = "ws://stream.meetup.com/2/rsvps"
var = []

def consumer(rsvp):
    pass


async def get_meetup_rsvps():
    async with websockets.connect(meet_up_stream) as websocket:
        counter = 1
        while counter <= 1:
            # for i in range(10):
            #while True:
            meetup_rsvp = await websocket.recv()
            # await consumer(message)
            # pprint(json.loads(meetup_rsvp))
            data = json.loads(meetup_rsvp)
            var.append(clean_meetup_result(data))
            # var.append(json.loads(meetup_rsvp))
            counter += 1

asyncio.get_event_loop().run_until_complete(get_meetup_rsvps())
pprint(var)



# https://pypi.org/project/websockets/
# http://websockets.readthedocs.io/en/stable/intro.html
# https://www.fullstackpython.com/websockets.html
# http://aiokafka.readthedocs.io/en/stable/
# https://github.com/dpkp/kafka-python
# http://kafka-python.readthedocs.io/en/master/
# https://kafka-python.readthedocs.io/en/master/usage.html