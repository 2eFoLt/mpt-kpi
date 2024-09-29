CREATE DATABASE IF NOT EXISTS mpt-kpi;  
USE mpt-kpi;

-- Creating the Role table
CREATE TABLE IF NOT EXISTS Role (
    Role_ID INT AUTO_INCREMENT PRIMARY KEY,
    Role_name VARCHAR(45) NOT NULL,
    Role_description VARCHAR(125)
);

-- Creating the Users table
CREATE TABLE IF NOT EXISTS Users (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_login VARCHAR(45) NOT NULL,
    User_password VARCHAR(100) NOT NULL,
    User_hash VARCHAR(100),
    Role_Role_ID INT,
    FOREIGN KEY (Role_Role_ID) REFERENCES Role(Role_ID)
);

-- Creating the Documents table
CREATE TABLE IF NOT EXISTS Documents (
    Document_ID INT AUTO_INCREMENT PRIMARY KEY,
    Document_hash VARCHAR(100) NOT NULL
);
