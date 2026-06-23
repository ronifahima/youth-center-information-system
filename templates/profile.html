{% extends "layout.html" %}

{% block content %}

<style>
    /* שדה אחיד לכל input / select / textarea */
    .form-field {
        width: 100%;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-size: 14px;
        box-sizing: border-box; /* חובה לרוחב זהה */
    }

    .form-label {
        font-weight: bold;
        display: block;
        margin-bottom: 8px;
    }

    .success-message {
        background: #e6f4ea;
        color: #1e7e34;
        padding: 14px;
        border-radius: 10px;
        margin-bottom: 25px;
        text-align: center;
        font-weight: bold;
    }
</style>

<!-- רקע אחיד -->
<div style="
    background:#f3e4d7;
    min-height:100vh;
    padding:60px 0;
">

    <!-- קוביית פתיחת פנייה (מוקטנת וממורכזת) -->
    <div style="
        max-width:600px;
        margin:0 auto;
        background:#ffffff;
        padding:40px;
        border-radius:20px;
        box-shadow:0 10px 25px rgba(0,0,0,0.15);
    ">

        <h2 style="text-align:center; margin-bottom:35px;">
            פתיחת פנייה חדשה
        </h2>

        <!-- הודעת הצלחה -->
        {% with messages = get_flashed_messages(with_categories=true) %}
          {% if messages %}
            {% for category, message in messages %}
              {% if category == 'success' %}
                <div class="success-message">
                    {{ message }}
                </div>
              {% endif %}
            {% endfor %}
          {% endif %}
        {% endwith %}

        <form method="POST" action="/open_request">

            <!-- נושא -->
            <div style="margin-bottom:25px;">
                <label class="form-label">נושא</label>

                <select name="subject" class="form-field" required>
                    <option value="">בחר נושא</option>
                    <option value="לימודים">לימודים</option>
                    <option value="מלגות">מלגות</option>
                    <option value="תעסוקה">תעסוקה</option>
                    <option value="אחר">אחר</option>
                </select>
            </div>

            <!-- תיאור הפנייה -->
            <div style="margin-bottom:35px;">
                <label class="form-label">תיאור הפנייה</label>

                <textarea name="description"
                          class="form-field"
                          rows="5"
                          required
                          placeholder="כתוב כאן את הפנייה שלך..."></textarea>
            </div>

            <!-- כפתור -->
            <div style="text-align:center;">
                <button type="submit"
                        style="
                            padding:12px 45px;
                            background:#c97a2b;
                            color:white;
                            border:none;
                            border-radius:10px;
                            font-size:16px;
                            cursor:pointer;
                        ">
                    פתיחת פנייה
                </button>
            </div>

        </form>

    </div>

</div>

{% endblock %}
