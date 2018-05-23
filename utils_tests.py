from json import load
from datetime import datetime
from unittest import TestCase, TestLoader, TextTestRunner
from utils import convert_milliseconds_since_epoch_time_local, clean_meetup_result


class EpochTimeConverterTestCase(TestCase):

    def setUp(self):
        self.time1 = 1526781485288
        self.time2 = 1526846400000

    def test_time1(self):
        expected_result = datetime(2018, 5, 19, 18, 58, 5)

        result = convert_milliseconds_since_epoch_time_local(time_value=self.time1)
        self.assertEqual(result, expected_result)

    def test_time2(self):
        expected_result = datetime(2018, 5, 20, 13, 0)

        result = convert_milliseconds_since_epoch_time_local(time_value=self.time2)
        self.assertEqual(result, expected_result)


class MeetUpRSVPCleanerTestCase(TestCase):

    def setUp(self):
        self.meetup_json_file0 = "example_data/example0.json"
        self.meetup_json_file1 = "example_data/example1.json"
        self.meetup_json_file2 = "example_data/example2.json"
        self.meetup_json_file3 = "example_data/example3.json"
        self.meetup_json_file4 = "example_data/example4.json"
        self.meetup_json_file5 = "example_data/example5.json"
        self.meetup_json_file6 = "example_data/example6.json"
        self.meetup_json_file7 = "example_data/example7.json"
        self.meetup_json_file8 = "example_data/example8.json"

        self.cleaned_keys = [
            'rsvp_id',
            'event_id',
            'event_name',
            'event_url',
            'group_city',
            'group_country',
            'group_id',
            'group_lat',
            'group_lon',
            'group_name',
            'group_state',
            'group_topics',
            'group_urlname',
            'member_id',
            'member_name',
            'venue_id',
            'venue_name',
            'rsvp_time',
            'event_time',
            'venue_lat',
            'venue_lon',
            'rsvp_response',
            'rsvp_guests',
            'rsvp_visibility',
            'member_photo',
            'member_other_services'
        ]

    def test_cleanup_on_one_row(self):

        expected_result = {
            'event_id': '250753032',
            'event_name': 'Welcome Walk',
            'event_time': datetime(2018, 5, 20, 13, 0),
            'event_url': 'https://www.meetup.com/Sierra-Club-Hiking-Meetup/events/250753032/',
            'group_city': 'Sunnyvale',
            'group_country': 'us',
            'group_id': 1809828,
            'group_lat': 37.35,
            'group_lon': -122.03,
            'group_name': 'Sierra Club Hiking Meetup',
            'group_state': 'CA',
            'group_topics': ['Fitness', 'Hiking', 'Outdoors', 'Social', 'Walking'],
            'group_urlname': 'Sierra-Club-Hiking-Meetup',
            'member_id': 73042492,
            'member_name': 'Kiran G',
            'member_photo': 'https://secure.meetupstatic.com/photos/member/5/0/e/5/thumb_277160709.jpeg',
            'rsvp_guests': 0,
            'rsvp_id': 1729035271,
            'rsvp_response': 'yes',
            'rsvp_time': datetime(2018, 5, 19, 18, 58, 5),
            'rsvp_visibility': 'public',
            'venue_id': 24356481,
            'venue_lat': 37.430397,
            'venue_lon': -122.086067,
            'venue_name': "Michael's at Shoreline",
            'member_other_services': []
        }

        with open(self.meetup_json_file0) as f:
            meetup_rsvp = load(f)
            cleaned_meetup_rsvp = clean_meetup_result(meetup_rsvp[0])
            self.assertEqual(cleaned_meetup_rsvp, expected_result)

    def test_cleanup_on_batch(self):

        with open(self.meetup_json_file8) as f:
            meetup_rsvps = load(f)
            for rsvp in meetup_rsvps:
                cleaned_rsvp = clean_meetup_result(rsvp)
                cleaned_rsvp_keys = list(cleaned_rsvp.keys())

                self.assertEqual(cleaned_rsvp_keys.sort(), self.cleaned_keys.sort())

time_test_suite = TestLoader().loadTestsFromTestCase(EpochTimeConverterTestCase)
TextTestRunner(verbosity=2).run(time_test_suite)

cleanup_test_suite = TestLoader().loadTestsFromTestCase(MeetUpRSVPCleanerTestCase)
TextTestRunner(verbosity=2).run(cleanup_test_suite)
