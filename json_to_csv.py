import csv
import json
from utils import clean_meetup_result


def json_to_dictionary(filename):
    with open(filename) as json_file:
        json_data = json.load(json_file)
    return json_data


def dictionary_to_csv(list_of_dictionaries, filename, field_names, delimiter=",", write_mode='w'):

    with open(filename, write_mode) as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter=delimiter)
        writer.writeheader()
        for row in list_of_dictionaries:
            writer.writerow(row)
        return len(list_of_dictionaries)


def dictionary_to_json(dictionary, write_to_file=False, filename=" ", write_mode='w'):
    if write_to_file:
        with open(filename, write_mode) as json_file:
            json_data = json.dump(dictionary, json_file, indent=4)
    else:
        json_data = json.dumps(dictionary, indent=4)
    return json_data


def dictionary_to_jsonl(documents):
    with open('example3_clean.jsonl', 'w') as f:
        for document in documents:
            f.write(json.dumps(document) + '\n')

filename = "example_data/example3.json"
export = "example6.csv"
flds = [
    'rsvp_id',
    'rsvp_time',
    'rsvp_response',
    'rsvp_guests',
    'rsvp_visibility',
    'event_id',
    'event_name',
    'event_time',
    'event_url',
    'member_id',
    'member_name',
    'member_photo',
    'member_other_services',
    'venue_id',
    'venue_name',
    'venue_lat',
    'venue_lon',
    'group_city',
    'group_country',
    'group_id',
    'group_lat',
    'group_lon',
    'group_name',
    'group_state',
    'group_topics',
    'group_urlname',
]

data_set = json_to_dictionary(filename)
from pprint import pprint

clean_data = []
for row in data_set:
    result = clean_meetup_result(row)
    clean_data.append(result)

print(len(clean_data))
# dictionary_to_csv(clean_data, filename=export, field_names=flds)
# dictionary_to_json(dictionary=clean_data, write_to_file=True, filename="example3_clean.json")
dictionary_to_jsonl(documents=clean_data)
