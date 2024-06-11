import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('alarm.db')
        self.cursor = self.connection.cursor()

    def get_alarms(self):
        query = "SELECT id, name, alarm_set, time_up, notify  FROM alarms"
        result = self.cursor.execute(query)
        alarms = result.fetchall()
        return alarms

    def add_alarm(self, text, time):
        try:
            query = f"INSERT INTO alarms(name, alarm_set) VALUES ('{text}', '{time}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def update_alarm(self, alarm_id, text, time):
        query = f"UPDATE alarms SET name = '{text}', alarm_set = '{time}' WHERE id = '{alarm_id}'"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_alarm(self, alarm_id):
        try:
            query = f"DELETE FROM alarms WHERE id = '{alarm_id}'"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def done_alarm(self, alarm_id):
        query = f"UPDATE alarms SET notify = '{1}' WHERE id = '{alarm_id}'"
        self.cursor.execute(query)
        self.connection.commit()