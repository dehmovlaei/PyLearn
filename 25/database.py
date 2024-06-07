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
            query = f"INSERT INTO alarm(name, time) VALUES ('{new_name}', '{new_time}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def update_alarm(self, new_name, new_time):
        query = f"UPDATE alarm SET name = '{new_name}' WHERE time = '{new_time}'"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_alarm(self, index):
        try:
            query = f"DELETE FROM alarm WHERE index = '{index}'"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False