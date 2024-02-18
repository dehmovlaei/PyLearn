import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('todo_list.db')
        self.cursor = self.connection.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_task(self):
        ...