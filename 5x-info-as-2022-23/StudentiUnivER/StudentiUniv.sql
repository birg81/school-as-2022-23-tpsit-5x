DROP DATABASE IF EXISTS Classe5FBoianoNunzio;
CREATE DATABASE IF NOT EXISTS Classe5FBoianoNunzio;
USE Classe5FBoianoNunzio;

-- tab studenti
DROP TABLE IF EXISTS Students;
CREATE TABLE IF NOT EXISTS Students(
	id INT PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(24) NOT NULL,
    lastname VARCHAR(24) NOT NULL,
    cf CHAR(16) UNIQUE NOT NULL,
    birthday DATE NOT NULL,
    -- questa è la matricola
    serialnumber VARCHAR (10) NOT NULL,
    gender CHAR(1) NOT NULL DEFAULT 'm'
);


INSERT INTO Students(firstname, lastname, cf, birthday, serialnumber, gender) VALUES
("Dario", "Sorrentino", "DS25VE102004","2004-10-25", "001", "m"),
("Nunzio", "Boiano", "BNONNZ26VC2004", "2004-08-26", "002", "m"),
("Imma", "Cioffi", "CFFMMI04L48Z001","2004-08-08", "003", "f");

-- tab subject
DROP TABLE IF EXISTS Subjects;
CREATE TABLE IF NOT EXISTS Subjects (
    id INT PRIMARY KEY AUTO_INCREMENT,
    courseName VARCHAR(32) NOT NULL,
    code CHAR(10) NOT NULL 
);
INSERT INTO Subjects(courseName, code) VALUES
("basi di dati","10078"),
("fondamenti di informatica", "10079");

-- tab corsi
DROP TABLE IF EXISTS Lessons;
CREATE TABLE IF NOT EXISTS Lessons (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dt DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    id_subject INT NOT NULL
);
    
-- tab esame
DROP TABLE IF EXISTS Exams;
CREATE TABLE IF NOT EXISTS Exams (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dt DATE NOT NULL DEFAULT CURRENT_DATE,
    fk_stud INT NOT NULL,
    fk_subject INT NOT NULL,
    grade INT NOT NULL CHECK (grade >=18 AND grade <= 30),
    FOREIGN KEY (fk_stud) REFERENCES Students(id)
    	ON DELETE CASCADE
    	ON UPDATE CASCADE,
    FOREIGN KEY (fk_subject) REFERENCES Subjects(id)
        ON DELETE CASCADE
    	ON UPDATE CASCADE
);
INSERT INTO Exams(fk_stud, fk_subject, grade) VALUES
(3, 2, 18),
(1, 1, 20);



-- Q selezionare studente esame e materie
SELECT
	s.firstname,
    s.lastname,
    e.grade,
    e.dt AS data,
    m.courseName as Materia
FROM
	students AS s,
    exams AS e,
    subjects as m
WHERE
	s.id = e.fk_stud AND
    e.fk_subject = m.id;
