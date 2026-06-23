from request import Request
from response import Response


class Youth:
    def __init__(self, id_number, first_name, last_name, phone):
        self.id_number = id_number
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

        # פרטי התחברות (לא חובה בתרשים, אבל קיימים במערכת)
        self.username = None
        self.password = None

    # קבלת שם משתמש וסיסמה
    def receive_username_password(self, username, password):
        self.username = username
        self.password = password

    # כניסה לשאלון קליטה (מימוש עתידי)
    def enter_intake_questionnaire(self):
        pass

    # עדכון מידע (טלפון)
    def update_details(self, phone):
        self.phone = phone

    # פתיחת פנייה חדשה
    def open_request(self, subject, description):
        return Request(
            user_id=self.id_number,
            subject=subject,
            description=description
        )
    # מענה לפנייה קיימת
    def reply_to_request(self, request_id, content):
        return Response(
            request_id=request_id,
            content=content,
            sender="צעיר"
        )
    # סגירת פנייה קיימת
    def close_request(self, request_id):
        req = Request(None, None, None)
        req.update_request_status("סגורה", request_id)
