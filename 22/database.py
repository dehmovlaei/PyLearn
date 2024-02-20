import sqlite3
class Database:
    def __init__(self):
        self.connection = sqlite3.connect('todo_list.db')
        self.cursor = self.connection.cursor()

    def get_tasks(self):
        query = "SELECT * FROM tasks ORDER BY is_done"
        result = self.cursor.execute(query)
        tasks = result.fetchall()
        return tasks

    def add_task(self, new_title, new_date, new_description, is_important):
        try:
            query = f"INSERT INTO tasks(title, date, description, priority) VALUES ('{new_title}', '{new_date}', '{new_description}', '{is_important}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def update_task(self, id, value):
        query = f"UPDATE tasks SET is_done = '{value}' WHERE id = '{id}'"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_task(self, id):
        try:
            query = f"DELETE FROM tasks WHERE id = '{id}'"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False