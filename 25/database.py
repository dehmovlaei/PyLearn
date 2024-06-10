import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('alarm.db')
        self.cursor = self.connection.cursor()

    def get_alarms(self):
        query = "SELECT id, name, time  FROM alarms"
        result = self.cursor.execute(query)
        alarms = result.fetchall()
        return alarms

    def add_alarm(self, text, time):
        try:
            query = f"INSERT INTO alarms(name, time) VALUES ('{text}', '{time}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def update_alarm(self, alarm_id, text, time):
        query = f"UPDATE alarms SET name = '{text}', time = '{time}' WHERE id = '{alarm_id}'"
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