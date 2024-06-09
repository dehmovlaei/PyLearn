import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('alarm.db')
        self.cursor = self.connection.cursor()

    def get_alarms(self):
        query = "SELECT * FROM alarms"
        result = self.cursor.execute(query)
        alarms = result.fetchall()
        return alarms

    def add_alarm(self, new_name, new_time):
        try:
            query = f"INSERT INTO alarms(name, time) VALUES ('{new_name}', '{new_time}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def update_alarm(self, new_name, new_time, alarm_id):
        query = f"UPDATE alarms SET name = '{new_name}', time = '{new_time}' WHERE id = '{alarm_id}'"
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