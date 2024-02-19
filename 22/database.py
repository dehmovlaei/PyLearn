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

    def add_task(self, new_title, new_description):
        try:
            query = f"INSERT INTO tasks(title, description) VALUES ('{new_title}', '{new_description}')"
            self.cursor.execute(query)
            self.connection.commit()
            return True
        except:
            return False

    def delete_task(self):
        query = "DELETE FROM"

    def update_task(selfself):
        query = "UPDATE tasks ... SET is_done = '1' WHERE"