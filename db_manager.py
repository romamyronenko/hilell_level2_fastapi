import sqlite3

from models import Task


class DBManager:
    def __init__(self, db):
        self._db = db

        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        self._cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS Tasks(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title VARCHAR(255),
                description VARCHAR(255),
                hours INTEGER,
                is_done BOOLEAN
            );
            """
        )

    def _execute(self, query):
        self._cursor.execute(query)
        self._conn.commit()

    def add_task(self, task: Task) -> None:
        self._execute(
            f"""
            INSERT INTO Tasks(title, description, hours, is_done)
            VALUES ('{task.title}', '{task.description}', {task.hours}, {task.is_done});
            """
        )

    def edit_task(self, id_, new_description):
        # self._execute(
        #     f"""
        #     UPDATE Tasks
        #     SET description='{new_description}'
        #     WHERE id={id_} AND user_id={user_id};
        #     """
        # )
        pass

    def delete_task(self, id_):
        self._execute(
            f"""
            DELETE
            FROM Tasks
            WHERE id={id_};
            """
        )

    def get_all_tasks(self) -> list[Task]:
        self._execute(
            f"""
            SELECT id, title, description, hours, is_done
            FROM Tasks;
            """
        )
        tasks = self._cursor.fetchall()
        result = []
        for task in tasks:
            result.append(Task(
                id=task[0],
                title=task[1],
                description=task[2],
                hours=task[3],
                is_done=task[4],
            ))
        return result

    def get_task(self, task_id):
        self._execute(
            f"""
                SELECT id, title, description, hours, is_done
                FROM Tasks
                WHERE id={task_id};
            """
        )
        task = self._cursor.fetchone()
        return Task(
            id=task[0],
            title=task[1],
            description=task[2],
            hours=task[3],
            is_done=task[4],
        )


db_manager = DBManager("database1")
