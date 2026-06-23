CREATE DATABASE youth_center_db;
USE youth_center_db;

-- ================================
-- טבלת משתמשים
-- ================================
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone VARCHAR(20)
) ENGINE=InnoDB;

-- ================================
-- הוספת משתמשים לדוגמה
-- ================================
INSERT INTO users (username, password, first_name, last_name, phone)
VALUES
('roni_p', '1234', 'רוני', 'פחימה', '0501234567'),
('daniel_k', 'abcd', 'דניאל', 'כהן', '0529876543'),
('noa_l', 'pass1', 'נועה', 'לוי', '0541112233');

-- ================================
-- טבלת פניות
-- ================================
CREATE TABLE requests (
    requests_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    subject VARCHAR(100) NOT NULL,
    description TEXT,
    status VARCHAR(30) DEFAULT 'פתוחה',
    opened_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    closed_at DATETIME NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
) ENGINE=InnoDB;

-- ================================
-- טבלת תגובות לפניות
-- ================================
CREATE TABLE responses (
    responses_id INT AUTO_INCREMENT PRIMARY KEY,
    request_id INT NOT NULL,
    content TEXT NOT NULL,
    sender VARCHAR(30) NOT NULL,
    response_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (request_id) REFERENCES requests(requests_id)
) ENGINE=InnoDB;

SELECT * FROM users;
SELECT * FROM requests;
SELECT * FROM responses;

DELETE FROM responses
WHERE responses_id > 0;

DELETE FROM requests
WHERE requests_id > 0;

ALTER TABLE requests AUTO_INCREMENT = 1;
ALTER TABLE responses AUTO_INCREMENT = 1;
