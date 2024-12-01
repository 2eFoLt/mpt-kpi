CREATE DATABASE IF NOT EXISTS mpt_kpi;
USE mpt_kpi;

CREATE TABLE IF NOT EXISTS Role (
    role_id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(45) NOT NULL,
    role_points INT NOT NULL,
    role_description VARCHAR(125)
);

CREATE TABLE IF NOT EXISTS Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(45) NOT NULL,
    user_surname VARCHAR(45) NOT NULL,
    user_patronymic VARCHAR(45) NOT NULL,
    user_email VARCHAR(45) NOT NULL,
    user_phone VARCHAR(45) NOT NULL,
    user_passhash VARCHAR(100) NOT NULL,
    user_role VARCHAR(100) NOT NULL,
    user_login VARCHAR(45) NOT NULL,
    is_admin BOOLEAN NOT NULL DEFAULT FALSE,
    role_role_id INT,
    FOREIGN KEY (role_role_id) REFERENCES Role(role_id)
);

CREATE TABLE IF NOT EXISTS Criteria (
    criteria_ID INT AUTO_INCREMENT PRIMARY KEY,
    criteria_name VARCHAR(255) NOT NULL,
    rating_from INT NOT NULL,
    score_before INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Certificates (
    certificate_ID INT AUTO_INCREMENT PRIMARY KEY,
    uploaded_by INT NOT NULL,
    criteria_id INT NOT NULL,
    is_approved BOOLEAN NOT NULL DEFAULT TRUE,
    rating INT NOT NULL,
    file_path VARCHAR(255) NOT NULL,
    FOREIGN KEY (uploaded_by) REFERENCES Users(user_id),
    FOREIGN KEY (criteria_id) REFERENCES Criteria(criteria_id)
);

INSERT INTO mpt_kpi.role VALUES ('1', 'Работник', '5', 'Работает');
INSERT INTO mpt_kpi.users VALUES ('1', 'Иван', 'Иванов', 'Иванович', 'IvanII@mail.ru', '79251232233', 'dsadxz', 'Работник', 'IvanII', '0', '1');
INSERT INTO mpt_kpi.criteria VALUES ('1', 'Доп. выходы', '1', '5');
INSERT INTO mpt_kpi.certificates VALUES ('1', '1', '1', '1', '5', 'file.path');