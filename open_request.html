{% extends "layout.html" %}

{% block content %}

<h2 style="margin-bottom:25px;">הפניות שלי</h2>

<!-- סינון לפי סטטוס -->
<form method="GET" action="/my_requests"
      style="display:flex; align-items:center; gap:15px; margin-bottom:30px;">

    <label style="font-weight:bold;">סינון לפי סטטוס:</label>

    <select name="status"
            style="padding:10px; border-radius:8px; border:1px solid #ccc; min-width:160px;">
        <option value="הכל" {% if selected_status == 'הכל' %}selected{% endif %}>הכל</option>
        <option value="פתוחה" {% if selected_status == 'פתוחה' %}selected{% endif %}>פתוחה</option>
        <option value="בטיפול" {% if selected_status == 'בטיפול' %}selected{% endif %}>בטיפול</option>
        <option value="סגורה" {% if selected_status == 'סגורה' %}selected{% endif %}>סגורה</option>
    </select>

    <button type="submit"
            style="background:#c97a2b; color:white; border:none; padding:10px 22px; border-radius:8px;">
        סינון
    </button>
</form>

{% if requests %}

    {% for req in requests %}
        <div style="
            background:#ffffff;
            border-radius:14px;
            padding:20px;
            margin-bottom:20px;
            box-shadow:0 4px 10px rgba(0,0,0,0.08);
            position:relative;
        ">

            <!-- כותרת + סטטוס -->
            <div style="display:flex; justify-content:space-between; align-items:center;">
                <strong>{{ req.subject }}</strong>

                <span style="
                    padding:6px 14px;
                    border-radius:20px;
                    font-size:13px;
                    background:
                        {% if req.status == 'פתוחה' %}#e6f0ff
                        {% elif req.status == 'בטיפול' %}#fff3cd
                        {% else %}#e6f7ec{% endif %};
                ">
                    {{ req.status }}
                </span>
            </div>

            <!-- תאריכי פנייה -->
            <div style="margin-top:8px; font-size:13px; color:#555;">
                <p>
                    <strong>תאריך פתיחת פנייה:</strong>
                    {{ req.opened_at.strftime('%d/%m/%Y %H:%M') }}
                </p>

                {% if req.closed_at %}
                    <p>
                        <strong>תאריך סגירת פנייה:</strong>
                        {{ req.closed_at.strftime('%d/%m/%Y %H:%M') }}
                    </p>
                {% endif %}
            </div>

            <!-- תיאור הפנייה -->
            <p style="margin-top:12px; font-size:14px;">
                {{ req.description }}
            </p>

            <!-- תגובות קיימות -->
            {% if req.responses %}
                <div style="
                    margin-top:15px;
                    padding:15px;
                    background:#f7f7f7;
                    border-radius:10px;
                    font-size:14px;
                    max-width:600px;
                ">
                    <strong>תגובות לפנייה:</strong>

                    {% for res in req.responses %}
                        <div style="margin-top:10px;">
                            <p style="margin:0;">
                                {{ res.content }}
                            </p>
                            <span style="font-size:12px; color:#777;">
                                נשלח ב־{{ res.response_date.strftime('%d/%m/%Y %H:%M') }}
                            </span>
                        </div>
                    {% endfor %}
                </div>
            {% endif %}

            <!-- תגובה חדשה -->
            {% if req.status != 'סגורה' %}
                <form method="POST" action="/response" style="margin-top:15px;">
                    <input type="hidden" name="request_id" value="{{ req.requests_id }}">

                    <div style="max-width:600px;">
                        <textarea
                            name="content"
                            rows="3"
                            placeholder="כתוב כאן תגובה לפנייה..."
                            style="width:100%; padding:10px; border-radius:8px; border:1px solid #ccc;"
                            required
                        ></textarea>

                        <button type="submit"
                                style="margin-top:8px; background:#c97a2b; color:white; border:none;
                                       padding:8px 20px; border-radius:8px;">
                            שליחת תגובה
                        </button>
                    </div>
                </form>

                <!-- כפתור סגירת פנייה -->
                <form method="POST" action="/close_request"
                      style="position:absolute; bottom:20px; left:20px;">
                    <input type="hidden" name="request_id" value="{{ req.requests_id }}">

                    <button type="submit"
                            onclick="return confirm('האם את בטוחה שברצונך לסגור את הפנייה?');"
                            style="
                                background:#d9534f;
                                color:white;
                                border:none;
                                padding:8px 18px;
                                border-radius:8px;
                                cursor:pointer;
                            ">
                        סגירת פנייה
                    </button>
                </form>
            {% endif %}

        </div>
    {% endfor %}

{% else %}
    <p>אין פניות להצגה.</p>
{% endif %}

{% endblock %}
