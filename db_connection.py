import mysql.connector

def get_db_connection():
    """
    פונקציה שמתחברת לבסיס הנתונים MySQL
    ומחזירה חיבור פתוח לבסיס הנתונים
    """

    connection = mysql.connector.connect(
        host="localhost",        # MySQL רץ על המחשב המקומי
        user="root",             # שם המשתמש ב-MySQL
        password="ronieue123!",# הסיסמה שלך ל-MySQL
        database="youth_center_db1"  # שם בסיס הנתונים שיצרת
    )

    return connection
