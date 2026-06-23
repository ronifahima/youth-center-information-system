from db_connection import get_db_connection


class Request:
    def __init__(self, user_id, subject, description):
        self.user_id = user_id
        self.subject = subject
        self.description = description
        self.status = "פתוחה"
        self.opened_at = None   # מתמלא אוטומטית ב-DB
        self.closed_at = None   # יתמלא בעת סגירת פנייה

    # פתיחת פנייה חדשה
    def send_request(self):
        connection = get_db_connection()
        cursor = connection.cursor()

        sql = """
        INSERT INTO requests
        (user_id, subject, description, status)
        VALUES (%s, %s, %s, %s)
        """

        cursor.execute(sql, (
            self.user_id,
            self.subject,
            self.description,
            self.status
        ))

        connection.commit()
        cursor.close()
        connection.close()

    # עדכון סטטוס פנייה (כולל תאריך סגירה)
    def update_request_status(self, new_status, request_id):
        connection = get_db_connection()
        cursor = connection.cursor()

        if new_status == "סגורה":
            sql = """
            UPDATE requests
            SET status = %s,
                closed_at = NOW()
            WHERE requests_id = %s
            """
            cursor.execute(sql, (new_status, request_id))
        else:
            sql = """
            UPDATE requests
            SET status = %s
            WHERE requests_id = %s
            """
            cursor.execute(sql, (new_status, request_id))

        connection.commit()
        cursor.close()
        connection.close()
