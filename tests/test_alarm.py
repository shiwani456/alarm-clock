import os
import unittest

from alarm import Alarm
from storage import AlarmStorage
from utils import parse_time


class TestAlarmClock(unittest.TestCase):

    TEST_FILE = "alarms.json"

    def setUp(self):
        # Start each test with a clean storage file
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

        self.storage = AlarmStorage()

    def tearDown(self):
        if os.path.exists(self.TEST_FILE):
            os.remove(self.TEST_FILE)

    def test_parse_time_24_hour(self):
        self.assertEqual(parse_time("14:30"), "14:30")

    def test_parse_time_12_hour(self):
        self.assertEqual(parse_time("2:30 PM"), "14:30")

    def test_invalid_time(self):
        with self.assertRaises(ValueError):
            parse_time("99:99")

    def test_save_and_load_alarm(self):
        alarm = Alarm(
            id=1,
            time="08:00",
            label="Morning Alarm",
            repeat=False,
            enabled=True
        )

        self.storage.save_alarms([alarm])

        alarms = self.storage.load_alarms()

        self.assertEqual(len(alarms), 1)
        self.assertEqual(alarms[0].id, 1)
        self.assertEqual(alarms[0].time, "08:00")
        self.assertEqual(alarms[0].label, "Morning Alarm")
        self.assertFalse(alarms[0].repeat)
        self.assertTrue(alarms[0].enabled)

    def test_get_next_id(self):
        alarm1 = Alarm(
            id=1,
            time="07:00",
            label="Gym",
            repeat=False,
            enabled=True
        )

        alarm2 = Alarm(
            id=2,
            time="09:00",
            label="Meeting",
            repeat=True,
            enabled=True
        )

        self.storage.save_alarms([alarm1, alarm2])

        self.assertEqual(self.storage.get_next_id(), 3)

    def test_alarm_string(self):
        alarm = Alarm(
            id=10,
            time="18:45",
            label="Dinner",
            repeat=True,
            enabled=True
        )

        expected = "[10] 18:45 | Daily | ON | Dinner"
        self.assertEqual(str(alarm), expected)


if __name__ == "__main__":
    unittest.main()