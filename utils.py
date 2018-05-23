import time
from datetime import datetime
from pprint import pprint


def convert_milliseconds_since_epoch_time_local(time_value, return_as_string=False):
    if time_value:
        if return_as_string:
            return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_value/1000))
        else:
            date_str = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_value/1000))
            return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')


def clean_meetup_result(data):
    # flatten
    keys_to_process = ["event", "group", "member", "venue"]
    for key in keys_to_process:
        if "venue" not in data:
            data["venue"] = {
                "lat": None,
                "lon": None,
                "venue_id": None,
                "venue_name": None
            }

        if "event" in data:
            if "time" not in data["event"]:
                data["event"]["time"] = None

        data.update(data[key])
        data.pop(key)

    # convert epoch to date
    data["rsvp_time"] = str(convert_milliseconds_since_epoch_time_local(data["mtime"]))
    data["event_time"] = str(convert_milliseconds_since_epoch_time_local(data["time"]))

    # Make array of group topics
    data["group_topics"] = sorted([row["topic_name"] for row in data["group_topics"]])

    # rename ambiguous keys
    data["venue_lat"] = data["lat"]
    data["venue_lon"] = data["lon"]
    data["rsvp_response"] = data["response"]
    data["rsvp_guests"] = data["guests"]
    data["rsvp_visibility"] = data["visibility"]

    if "group_state" not in data:
        data["group_state"] = None
    # if "group_topics" not in data:
    #     data["group_topics"] = []

    if "photo" in data:
        data["member_photo"] = data["photo"]
        data.pop("photo")
    else:
        data["member_photo"] = None

    if "other_services" not in data:
        data["member_other_services"] = []
    else:
        data["member_other_services"] = data["other_services"]
        data.pop("other_services")

    # Remove last batch of keys
    keys_to_remove = ["lat", "lon", "mtime", "time", "response", "guests", "visibility"]
    for key in keys_to_remove:
        data.pop(key)
    return data
