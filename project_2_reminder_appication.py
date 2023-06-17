from plyer import notification
import datetime


class Reminder:
    def __init__(self):
        self.reminders = []

    def set_reminder(self, reminder_text, reminder_time):
        reminder = {
            'text': reminder_text,
            'time': reminder_time
        }
        self.reminders.append(reminder)

    def check_reminders(self):
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for reminder in self.reminders:
            if current_time >= reminder['time']:
                self.send_notification(reminder['text'])
                self.reminders.remove(reminder)

    def send_notification(self, text):
        notification.notify(
            title='Reminder',
            message=text,
            timeout=10
        )
reminder_app = Reminder()

reminder_app.set_reminder("Meeting with clients", "2023-06-17 10:28:00")
reminder_app.set_reminder("Submit the report", "2023-06-18 09:00:00")

while True:
    reminder_app.check_reminders()
