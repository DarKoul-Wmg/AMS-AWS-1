create database if not exists callcenter_prueba;
use callcenter_prueba;

DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS employee;
DROP TABLE IF EXISTS call_outcome;
DROP TABLE IF EXISTS phone_call;
DROP TABLE IF EXISTS city;

CREATE TABLE IF NOT EXISTS city(
	id INT AUTO_INCREMENT PRIMARY KEY,
    city_name VARCHAR(128) NOT NULL
    
);

CREATE TABLE IF NOT EXISTS customer(
	id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(255) NOT NULL,
    city_id INT NOT NULL,
    customer_address VARCHAR(255) NOT NULL,
    next_call DATETIME NULL,
    ts_inserted DATETIME NOT NULL,
    CONSTRAINT city_id FOREIGN KEY (city_id) REFERENCES city(id)
);

CREATE TABLE IF NOT EXISTS 	employee(
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL
);
CREATE TABLE IF NOT EXISTS 	call_outcome(
	id INT AUTO_INCREMENT PRIMARY KEY,
    outcome_text VARCHAR(128) NOT NULL,
    CONSTRAINT outcome_text CHECK (outcome_text IN ('call started','finished - successfully','finished - unsuccessfully'))
);
CREATE TABLE IF NOT EXISTS 	phone_call(
	id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT NOT NULL,
    customer_id INT NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME NULL,
    call_outcome_id INT NULL,
    CONSTRAINT employee_id FOREIGN KEY (employee_id) REFERENCES employee(id),
    CONSTRAINT customer_id FOREIGN KEY (customer_id) REFERENCES customer(id),
    CONSTRAINT call_outcome_id FOREIGN KEY (call_outcome_id) REFERENCES call_outcome(id)
    );