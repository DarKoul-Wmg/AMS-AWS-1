SET AUTOCOMMIT=1;

CREATE DATABASE IF NOT EXISTS videoclub;

USE videoclub; 

CREATE TABLE GENERE (
	CodiGenere 	INT(5) PRIMARY KEY, 
	Descripcio 	VARCHAR(15) );

CREATE TABLE ACTOR (
	CodiActor	INT(5) PRIMARY KEY,
	Nom 		VARCHAR(15) ); 

CREATE TABLE PELICULA (
	CodiPeli	INT(5) PRIMARY KEY,
	Titol		VARCHAR(50),
	CodiGenere	INT(5),
	SegonaPart	INT(5),
	INDEX IDX_PELI_GEN (CodiGenere),
	INDEX IDX_PELI_SEGP (SegonaPart),
        FOREIGN KEY (CodiGenere) REFERENCES GENERE(CodiGenere),
        FOREIGN KEY (SegonaPart) REFERENCES PELICULA(CodiPeli));

CREATE TABLE INTERPRETADA (
	CodiPeli 	INT(5), 
	CodiActor	INT(5),
	PRIMARY KEY (CodiPeli, CodiActor), 
        INDEX IDX_PELIINTERPRETADA (CodiPeli),
        INDEX IDX_ACTORINTERPRETADA (CodiActor),
        FOREIGN KEY (CodiPeli) REFERENCES PELICULA(CodiPeli),
        FOREIGN KEY (CodiActor) REFERENCES ACTOR(CodiActor) );

CREATE TABLE COPIA (
	CodiPeli 	INT(5),
	CodiCopia 	INT(5),
	PRIMARY KEY (CodiPeli, CodiCopia),
	INDEX IDX_COPIA_PELI (CodiPeli),
	FOREIGN KEY (CodiPeli) REFERENCES PELICULA (CodiPeli)  );

CREATE TABLE CLIENT (
	DNI 		CHAR (10) PRIMARY KEY,
	Nom 		VARCHAR(20), 
	Adreca		VARCHAR(20), 
	Telefon 	CHAR (9) );

CREATE TABLE PRESTEC (
	CodiPeli	INT(5), 
	CodiCopia	INT(5), 
	Data		DATE, 
	DNI 		CHAR (10) ,
	PRIMARY KEY (CodiPeli, CodiCopia, Data),
        INDEX IDX_PRESTEC_CLIENT (DNI),
	FOREIGN KEY (DNI) REFERENCES CLIENT(DNI),
	FOREIGN KEY (CodiPeli,CodiCopia) REFERENCES COPIA(CodiPeli,CodiCopia) );

INSERT INTO GENERE VALUES (1, 'Terror');
INSERT INTO GENERE VALUES (2, 'Comic');
INSERT INTO GENERE VALUES (3, 'Drama');

INSERT INTO ACTOR VALUES (1, 'Alex Brown');
INSERT INTO ACTOR VALUES (2, 'Michelle Docker');
INSERT INTO ACTOR VALUES (3, 'Fanny Lloyd');

INSERT INTO PELICULA VALUES (1, 'La venganza de los zombies', 2, NULL);
INSERT INTO PELICULA VALUES (2, 'Anem a treballar', 2, NULL);
INSERT INTO PELICULA VALUES (3, 'Anem al cinema', 1, 2);
INSERT INTO PELICULA VALUES (4, 'Som els milors', 3, NULL);
INSERT INTO PELICULA VALUES (5, 'We are the world', 2, 1);

INSERT INTO INTERPRETADA VALUES (1,1);
INSERT INTO INTERPRETADA VALUES (1,2);
INSERT INTO INTERPRETADA VALUES (2,1);
INSERT INTO INTERPRETADA VALUES (2,2);
INSERT INTO INTERPRETADA VALUES (3,1);
INSERT INTO INTERPRETADA VALUES (4,3);
INSERT INTO INTERPRETADA VALUES (5,3);
INSERT INTO INTERPRETADA VALUES (3,2);
INSERT INTO INTERPRETADA VALUES (4,2);
INSERT INTO INTERPRETADA VALUES (5,2);

INSERT INTO COPIA VALUES (1, 1);
INSERT INTO COPIA VALUES (1, 2);
INSERT INTO COPIA VALUES (2, 1);
INSERT INTO COPIA VALUES (2, 2);
INSERT INTO COPIA VALUES (3, 1);
INSERT INTO COPIA VALUES (3, 2);
INSERT INTO COPIA VALUES (3, 3);
INSERT INTO COPIA VALUES (4, 1);
INSERT INTO COPIA VALUES (5, 1);

INSERT INTO CLIENT VALUES ('011111111Z', 'Pere Puig Roig', NULL, '934444444');
INSERT INTO CLIENT VALUES ('022222222R', 'Maria Catasus Comas', NULL, '555666111');

INSERT INTO PRESTEC VALUES (1, 1, '2019-02-25', '011111111Z');
INSERT INTO PRESTEC VALUES (2, 1, '2019-03-01', '022222222R');
INSERT INTO PRESTEC VALUES (1, 2, '2019-03-02', '022222222R');
INSERT INTO PRESTEC VALUES (2, 2, '2019-03-02', '022222222R');
INSERT INTO PRESTEC VALUES (3, 1, '2019-03-02', '022222222R');
INSERT INTO PRESTEC VALUES (2, 1, '2019-03-11', '011111111Z');
INSERT INTO PRESTEC VALUES (1, 2, '2019-03-12', '011111111Z');
INSERT INTO PRESTEC VALUES (2, 2, '2019-03-14', '011111111Z');
INSERT INTO PRESTEC VALUES (3, 1, '2019-03-22', '011111111Z');
