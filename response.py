from db_connection import get_db_connection

class Response:
    def __init__(self, request_id, content, sender):
        self.request_id = request_id
        self.content = content
        self.sender = sender

    def send_response(self):
        connection = get_db_connection()
        cursor = connection.cursor()

        sql = """
        INSERT INTO responses
        (request_id, content, sender)
        VALUES (%s, %s, %s)
        """

        cursor.execute(sql, (
            self.request_id,
            self.content,
            self.sender
        ))

        connection.commit()
        cursor.close()
        connection.close()
