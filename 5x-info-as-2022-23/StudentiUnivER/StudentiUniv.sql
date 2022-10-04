DROP DATABASE IF EXISTS Classe5FBoianoNunzio;
CREATE DATABASE IF NOT EXISTS Classe5FBoianoNunzio;
USE Classe5FBoianoNunzio;

-- tab studenti
DROP TABLE IF EXISTS Studenti;
CREATE TABLE IF NOT EXISTS Studenti(
	id INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(24) NOT NULL,
    lastname VARCHAR(24) NOT NULL,
    cf CHAR(16) UNIQUE NOT NULL,
    birthday DATE NOT NULL,
    -- questa è la matricola
    serialnumber VARCHAR (10) NOT NULL,
    gender CHAR(1) NOT NULL DEFAULT 'm'
);


INSERT INTO Studenti(firstname, lastname, cf, birthday, serialnumber, gender) VALUES
("Dario", "Sorrentino", "DS25VE102004","2004-10-25", "001", "m"),
("Nunzio", "Boiano", "BNONNZ26VC2004", "2004-08-26", "002", "m"),
("Imma", "Cioffi", "CFFMMI04L48Z001","2004-08-08", "003", "f");