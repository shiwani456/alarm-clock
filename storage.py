import json
import os

from alarm import Alarm


class AlarmStorage:
    FILE_NAME = "alarms.json"

    def __init__(self):
        if not os.path.exists(self.FILE_NAME):
            with open(self.FILE_NAME, "w") as f:
                json.dump([], f)

    def load_alarms(self):
        try:
            with open(self.FILE_NAME, "r") as f:
                data = json.load(f)

            return [Alarm.from_dict(item) for item in data]

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_alarms(self, alarms):
        with open(self.FILE_NAME, "w") as f:
            json.dump(
                [alarm.to_dict() for alarm in alarms],
                f,
                indent=4
            )

    def get_next_id(self):
        alarms = self.load_alarms()

        if not alarms:
            return 1

        return max(a.id for a in alarms) + 1