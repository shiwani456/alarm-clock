# Python CLI Alarm Clock

A simple, object-oriented Alarm Clock built in Python that runs entirely in the command line. The application allows users to create, manage, and execute alarms with persistent JSON storage.

## Features

* Add new alarms
* List all alarms
* Delete alarms
* Enable or disable alarms
* Daily repeating alarms
* Snooze alarms (5 minutes)
* Cross-platform alarm notification
* JSON-based persistence (no database required)
* Object-Oriented Design
* Modular project structure

---

## Project Structure

```text
alarm-clock/
│
├── main.py              # Application entry point
├── cli.py               # Command-line interface
├── alarm.py             # Alarm model
├── scheduler.py         # Alarm scheduler
├── storage.py           # JSON storage
├── utils.py             # Utility functions
├── alarms.json          # Automatically created
├── requirements.txt
├── README.md
└── tests/
    └── test_alarm.py
```

---

## Requirements

* Python 3.9 or higher
* No third-party libraries

---

## Installation

Clone the repository:

```bash
git clone https://github.com/<your-username>/alarm-clock.git
cd alarm-clock
```

(Optional) Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Running the Application

Start the application:

```bash
python main.py
```

You will see a menu similar to:

```text
========================================
      PYTHON ALARM CLOCK
========================================

1. Add Alarm
2. List Alarms
3. Delete Alarm
4. Enable / Disable Alarm
5. Run Alarm Scheduler
6. Exit
```

---

## Usage

### Add an Alarm

Choose option **1** and provide:

* Time (`HH:MM` or `HH:MM AM/PM`)
* Alarm label
* Whether the alarm should repeat daily

Example:

```text
Time: 07:30 AM
Label: Morning Workout
Repeat Daily? y
```

---

### List Alarms

Choose option **2**.

Example output:

```text
[1] 07:30 | Daily | ON | Morning Workout
[2] 21:00 | Once  | ON | Medicine
```

---

### Delete an Alarm

Choose option **3** and enter the alarm ID.

---

### Enable / Disable an Alarm

Choose option **4** and enter the alarm ID.

---

### Run the Scheduler

Choose option **5**.

The scheduler continuously checks the current time and triggers alarms when their scheduled time is reached.

When an alarm fires:

```text
=========================================
🔔 ALARM 🔔
=========================================
Time : 07:30
Label: Morning Workout
=========================================

1. Snooze 5 minutes
2. Dismiss
```

---

## Data Storage

All alarms are stored in a local JSON file named `alarms.json`.

Example:

```json
[
  {
    "id": 1,
    "time": "07:30",
    "label": "Morning Workout",
    "repeat": true,
    "enabled": true
  }
]
```

---

## Running Tests

Run the unit tests with:

```bash
python -m unittest discover
```

or

```bash
python -m unittest test_alarm.py
```

Expected output:

```text
......
----------------------------------------------------------------------
Ran 6 tests in 0.01s

OK
```

---

## Technologies Used

* Python 3
* Object-Oriented Programming (OOP)
* JSON
* Dataclasses
* `datetime`
* `unittest`

---

## Future Improvements

* Command-line arguments using `argparse`
* Weekly and monthly recurring alarms
* Desktop notifications
* Custom snooze duration
* Multiple alarm sounds
* Time zone support
* Logging
* Better scheduler logic to avoid duplicate triggers
* Additional unit and integration tests

---

## Author

Developed as a Python CLI application to demonstrate:

* Object-Oriented Design
* File handling
* JSON persistence
* Modular architecture
* Command-line interface development
* Basic scheduling concepts
