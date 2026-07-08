from alarm import Alarm
from storage import AlarmStorage
from scheduler import AlarmScheduler
from utils import parse_time


class AlarmCLI:

    def __init__(self):
        self.storage = AlarmStorage()

    def start(self):

        while True:
            self.show_menu()

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_alarm()

            elif choice == "2":
                self.list_alarms()

            elif choice == "3":
                self.delete_alarm()

            elif choice == "4":
                self.toggle_alarm()

            elif choice == "5":
                self.run_scheduler()

            elif choice == "6":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.\n")

    def show_menu(self):
        print("\n" + "=" * 40)
        print("      PYTHON ALARM CLOCK")
        print("=" * 40)
        print("1. Add Alarm")
        print("2. List Alarms")
        print("3. Delete Alarm")
        print("4. Enable / Disable Alarm")
        print("5. Run Alarm Scheduler")
        print("6. Exit")

    def add_alarm(self):

        try:
            time = parse_time(
                input("Enter time (HH:MM or HH:MM AM/PM): ")
            )

            label = input("Label: ").strip()

            repeat = (
                input("Repeat Daily? (y/n): ")
                .strip()
                .lower()
            ) == "y"

            alarm = Alarm(
                id=self.storage.get_next_id(),
                time=time,
                label=label,
                repeat=repeat,
                enabled=True
            )

            alarms = self.storage.load_alarms()
            alarms.append(alarm)
            self.storage.save_alarms(alarms)

            print("\nAlarm added successfully!")

        except ValueError as e:
            print(e)

    def list_alarms(self):

        alarms = self.storage.load_alarms()

        if not alarms:
            print("\nNo alarms found.")
            return

        print("\nCurrent Alarms")
        print("-" * 70)

        for alarm in alarms:
            print(alarm)

    def delete_alarm(self):

        alarms = self.storage.load_alarms()

        if not alarms:
            print("\nNo alarms available.")
            return

        self.list_alarms()

        try:
            alarm_id = int(
                input("\nEnter Alarm ID to delete: ")
            )

            alarms = [
                alarm
                for alarm in alarms
                if alarm.id != alarm_id
            ]

            self.storage.save_alarms(alarms)

            print("Alarm deleted.")

        except ValueError:
            print("Invalid ID.")

    def toggle_alarm(self):

        alarms = self.storage.load_alarms()

        if not alarms:
            print("\nNo alarms available.")
            return

        self.list_alarms()

        try:
            alarm_id = int(
                input("\nAlarm ID: ")
            )

            found = False

            for alarm in alarms:
                if alarm.id == alarm_id:
                    alarm.enabled = not alarm.enabled
                    found = True
                    break

            if found:
                self.storage.save_alarms(alarms)
                print("Alarm updated.")
            else:
                print("Alarm not found.")

        except ValueError:
            print("Invalid ID.")

    def run_scheduler(self):

        print("\nStarting Scheduler...\n")

        scheduler = AlarmScheduler()
        scheduler.run()