import asyncio
import websockets
import json

meet_up_stream = "ws://stream.meetup.com/2/rsvps"
number_of_rows = 25000
json_dump_file_name = "example8.json"

list_of_rows = []

async def get_meetup_rsvps():
    async with websockets.connect(meet_up_stream) as websocket:
        counter = 1
        while counter <= number_of_rows:
            meetup_rsvp = await websocket.recv()
            list_of_rows.append(json.loads(meetup_rsvp))
            counter += 1

asyncio.get_event_loop().run_until_complete(get_meetup_rsvps())

with open(json_dump_file_name, 'w') as outfile:
    json.dump(list_of_rows, outfile, indent=4, sort_keys=True)
