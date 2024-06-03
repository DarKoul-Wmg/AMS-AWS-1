create database if not exists vet_clinic_molina_william;
use vet_clinic_molina_william;

CREATE TABLE IF NOT EXISTS veterinarian(
	id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255) NULL,
    last_name VARCHAR(255) NULL,
    contact_number VARCHAR(20) NULL,
    email VARCHAR(255) NULL,
    specialization VARCHAR(255) NULL
    
);

CREATE TABLE IF NOT EXISTS owner(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    first_name VARCHAR(255) NULL,
    last_name VARCHAR(255) NULL,
    contact_number VARCHAR(20) NULL,
    email VARCHAR(255) NULL
);

CREATE TABLE IF NOT EXISTS 	animal(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    name VARCHAR(255) NULL,
    species VARCHAR(255) NULL,
    breed VARCHAR(255) NULL,
    owner_id INT NULL,
    birth_date DATE NULL,
    CONSTRAINT owner_id FOREIGN KEY (owner_id) REFERENCES owner(id)
	);

CREATE TABLE IF NOT EXISTS 	appointment(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    veterinarian_id INT NULL,
    animal_id INT NULL,
    appointment_date DATETIME NULL,
    reason VARCHAR(255) NULL,
    CONSTRAINT veterinarian_id FOREIGN KEY (veterinarian_id) REFERENCES veterinarian(id),
    CONSTRAINT animal_id FOREIGN KEY (animal_id) REFERENCES animal(id)
);

CREATE TABLE IF NOT EXISTS 	invoice(
	id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
    appointment_id INT NULL,
    total_amount DECIMAL(9,2) NULL,
    payment_status VARCHAR(20) NULL,
    CONSTRAINT appointment_id FOREIGN KEY (appointment_id) REFERENCES appointment(id)
);