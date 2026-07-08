import time
from datetime import datetime, timedelta

from storage import AlarmStorage
from utils import beep


class AlarmScheduler:

    def __init__(self):
        self.storage = AlarmStorage()

    def run(self):
        print("\nAlarm scheduler started...")
        print("Press Ctrl+C to stop.\n")

        try:
            while True:
                alarms = self.storage.load_alarms()

                now = datetime.now().strftime("%H:%M")

                for alarm in alarms:

                    if not alarm.enabled:
                        continue

                    if alarm.time == now:
                        self.trigger_alarm(alarm)

                        if alarm.repeat:
                            tomorrow = (
                                datetime.now() + timedelta(days=1)
                            )

                            alarm.time = tomorrow.strftime("%H:%M")

                        else:
                            alarm.enabled = False

                        self.storage.save_alarms(alarms)

                time.sleep(1)

        except KeyboardInterrupt:
            print("\nScheduler stopped.")

    def trigger_alarm(self, alarm):

        while True:

            print("\n")
            print("=" * 45)
            print("🔔 ALARM 🔔")
            print("=" * 45)
            print(f"Time : {alarm.time}")
            print(f"Label: {alarm.label}")
            print("=" * 45)

            beep()

            print("\n1. Snooze 5 minutes")
            print("2. Dismiss")

            choice = input("Choice: ").strip()

            if choice == "1":
                self.snooze(alarm)
                break

            elif choice == "2":
                print("Alarm dismissed.")
                break

            else:
                print("Invalid option.")

    def snooze(self, alarm):

        new_time = (
            datetime.now() + timedelta(minutes=5)
        ).strftime("%H:%M")

        alarm.time = new_time

        alarms = self.storage.load_alarms()

        for i in range(len(alarms)):
            if alarms[i].id == alarm.id:
                alarms[i] = alarm
                break

        self.storage.save_alarms(alarms)

        print(f"Alarm snoozed until {new_time}")