DROP DATABASE IF EXISTS `universitat`;
CREATE DATABASE `universitat` CHARACTER SET utf8mb4;
USE `universitat`;
 
CREATE TABLE `departament`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(50) NOT NULL
);

CREATE TABLE `persona`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `nif` VARCHAR(9) UNIQUE,
    `nom` VARCHAR(25) NOT NULL,
    `cognom1` VARCHAR(50) NOT NULL,
    `cognom2` VARCHAR(50),
    `ciutat` VARCHAR(25) NOT NULL,
    `adreca` VARCHAR(50) NOT NULL,
    `telefon` VARCHAR(9),
    `data_naixement` DATE NOT NULL,
    `sexe` ENUM('H', 'M') NOT NULL,
    `tipus` ENUM('professor', 'alumne') NOT NULL
);
 
CREATE TABLE `professor`(
    `id_professor` INT UNSIGNED PRIMARY KEY,
    `id_departament`  INT UNSIGNED NOT NULL,
    FOREIGN KEY (`id_professor`) REFERENCES persona(`id`),
    FOREIGN KEY (`id_departament` ) REFERENCES departament(`id`)
);
 
 CREATE TABLE `grau`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(100) NOT NULL
);
 
CREATE TABLE `assignatura` (
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `nom` VARCHAR(100) NOT NULL,
    `credits` FLOAT UNSIGNED NOT NULL,
    `tipus` ENUM('bàsica', 'obligatòria', 'optativa') NOT NULL,
    `curs` TINYINT UNSIGNED NOT NULL,
    `quatrimestre` TINYINT UNSIGNED NOT NULL,
    `id_professor` INT UNSIGNED,
    `id_grau`  INT UNSIGNED NOT NULL,
    FOREIGN KEY(`id_professor`) REFERENCES professor(`id_professor`),
    FOREIGN KEY(`id_grau` ) REFERENCES grau(`id`)
);
 
CREATE TABLE `curs_escolar`(
    `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    `any_inici` YEAR NOT NULL,
    `any_fi` YEAR NOT NULL
);

CREATE TABLE `alumne_es_matricula_assignatura` (
    `id_alumne`  INT UNSIGNED NOT NULL,
    `id_assignatura`  INT UNSIGNED NOT NULL,
    `id_curs_escolar`  INT UNSIGNED NOT NULL,
    PRIMARY KEY (`id_alumne` , `id_assignatura` , `id_curs_escolar` ),
    FOREIGN KEY (`id_alumne` ) REFERENCES persona(`id`),
    FOREIGN KEY (`id_assignatura` ) REFERENCES `assignatura`(`id`),
    FOREIGN KEY (`id_curs_escolar` ) REFERENCES curs_escolar(`id`)
);
 
 /* `departament`*/
INSERT INTO `departament` VALUES (1, 'Informàtica');
INSERT INTO `departament` VALUES (2, 'Matemàtiques');
INSERT INTO `departament` VALUES (3, 'Economia i Empresa');
INSERT INTO `departament` VALUES (4, 'Educació');
INSERT INTO `departament` VALUES (5, 'Agronomia');
INSERT INTO `departament` VALUES (6, 'Química i Física');
INSERT INTO `departament` VALUES (7, 'Filologia');
INSERT INTO `departament` VALUES (8, 'Dret');
INSERT INTO `departament` VALUES (9, 'Biologia i Geologia');
 
 /* `persona`*/
INSERT INTO `persona` VALUES (1, '26902806M', 'Salvador', 'Sánchez', 'Pérez', 'Almería', 'C/ Real del barrio alto', '950254837', '1991/03/28', 'H', 'alumne');
INSERT INTO `persona` VALUES (2, '89542419S', 'Juan', 'Saez', 'Vega', 'Almería', 'C/ Mercurio', '618253876', '1992/08/08', 'H', 'alumne');
INSERT INTO `persona` VALUES (3, '11105554G', 'Zoe', 'Ramirez', 'Gea', 'Almería', 'C/ Marte', '618223876', '1979/08/19', 'M', 'professor');
INSERT INTO `persona` VALUES (4, '17105885A', 'Pedro', 'Heller', 'Pagac', 'Almería', 'C/ Estrella fugaz', NULL, '2000/10/05', 'H', 'alumne');
INSERT INTO `persona` VALUES (5, '38223286T', 'David', 'Schmidt', 'Fisher', 'Almería', 'C/ Venus', '678516294', '1978/01/19', 'H', 'professor');
INSERT INTO `persona` VALUES (6, '04233869Y', 'José', 'Koss', 'Bayer', 'Almería', 'C/ Júpiter', '628349590', '1998/01/28', 'H', 'alumne');
INSERT INTO `persona` VALUES (7, '97258166K', 'Ismael', 'Strosin', 'Turcotte', 'Almería', 'C/ Neptuno', NULL, '1999/05/24', 'H', 'alumne');
INSERT INTO `persona` VALUES (8, '79503962T', 'Cristina', 'Lemke', 'Rutherford', 'Almería', 'C/ Saturno', '669162534', '1977/08/21', 'M', 'professor');
INSERT INTO `persona` VALUES (9, '82842571K', 'Ramón', 'Herzog', 'Tremblay', 'Almería', 'C/ Urano', '626351429', '1996/11/21', 'H', 'alumne');
INSERT INTO `persona` VALUES (10, '61142000L', 'Esther', 'Spencer', 'Lakin', 'Almería', 'C/ Plutón', NULL, '1977/05/19', 'M', 'professor');
INSERT INTO `persona` VALUES (11, '46900725E', 'Daniel', 'Herman', 'Pacocha', 'Almería', 'C/ Andarax', '679837625', '1997/04/26', 'H', 'alumne');
INSERT INTO `persona` VALUES (12, '85366986W', 'Carmen', 'Streich', 'Hirthe', 'Almería', 'C/ Almanzora', NULL, '1971-04-29', 'M', 'professor');
INSERT INTO `persona` VALUES (13, '73571384L', 'Alfredo', 'Stiedemann', 'Morissette', 'Almería', 'C/ Guadalquivir', '950896725', '1980/02/01', 'H', 'professor');
INSERT INTO `persona` VALUES (14, '82937751G', 'Manolo', 'Hamill', 'Kozey', 'Almería', 'C/ Duero', '950263514', '1977/01/02', 'H', 'professor');
INSERT INTO `persona` VALUES (15, '80502866Z', 'Alejandro', 'Kohler', 'Schoen', 'Almería', 'C/ Tajo', '668726354', '1980/03/14', 'H', 'professor');
INSERT INTO `persona` VALUES (16, '10485008K', 'Antonio', 'Fahey', 'Considine', 'Almería', 'C/ Sierra de los Filabres', NULL, '1982/03/18', 'H', 'professor');
INSERT INTO `persona` VALUES (17, '85869555K', 'Guillermo', 'Ruecker', 'Upton', 'Almería', 'C/ Sierra de Gádor', NULL, '1973/05/05', 'H', 'professor');
INSERT INTO `persona` VALUES (18, '04326833G', 'Micaela', 'Monahan', 'Murray', 'Almería', 'C/ Veleta', '662765413', '1976/02/25', 'H', 'professor');
INSERT INTO `persona` VALUES (19, '11578526G', 'Inma', 'Lakin', 'Yundt', 'Almería', 'C/ Picos de Europa', '678652431', '1998/09/01', 'M', 'alumne');
INSERT INTO `persona` VALUES (20, '79221403L', 'Francesca', 'Schowalter', 'Muller', 'Almería', 'C/ Quinto pino', NULL, '1980/10/31', 'H', 'professor');
INSERT INTO `persona` VALUES (21, '79089577Y', 'Juan', 'Gutiérrez', 'López', 'Almería', 'C/ Los pinos', '678652431', '1998/01/01', 'H', 'alumne');
INSERT INTO `persona` VALUES (22, '41491230N', 'Antonio', 'Domínguez', 'Guerrero', 'Almería', 'C/ Cabo de Gata', '626652498', '1999/02/11', 'H', 'alumne');
INSERT INTO `persona` VALUES (23, '64753215G', 'Irene', 'Hernández', 'Martínez', 'Almería', 'C/ Zapillo', '628452384', '1996/03/12', 'M', 'alumne');
INSERT INTO `persona` VALUES (24, '85135690V', 'Sonia', 'Gea', 'Ruiz', 'Almería', 'C/ Mercurio', '678812017', '1995/04/13', 'M', 'alumne');
 
/* `professor`*/
INSERT INTO `professor` VALUES (3, 1);
INSERT INTO `professor` VALUES (5, 2);
INSERT INTO `professor` VALUES (8, 3);
INSERT INTO `professor` VALUES (10, 4);
INSERT INTO `professor` VALUES (12, 4);
INSERT INTO `professor` VALUES (13, 6);
INSERT INTO `professor` VALUES (14, 1);
INSERT INTO `professor` VALUES (15, 2);
INSERT INTO `professor` VALUES (16, 3);
INSERT INTO `professor` VALUES (17, 4);
INSERT INTO `professor` VALUES (18, 5);
INSERT INTO `professor` VALUES (20, 6);
 
 /* `grau`*/
INSERT INTO `grau` VALUES (1, 'grau en Enginyeria Agrícola (Pla 2015)');
INSERT INTO `grau` VALUES (2, 'grau en Enginyeria Elèctrica (Pla 2014)');
INSERT INTO `grau` VALUES (3, 'grau en Enginyeria Electrònica Industrial (Pla 2010)');
INSERT INTO `grau` VALUES (4, 'grau en Enginyeria Informàtica (Pla 2015)');
INSERT INTO `grau` VALUES (5, 'grau en Enginyeria Mecànica (Pla 2010)');
INSERT INTO `grau` VALUES (6, 'grau en Enginyeria Química Industrial (Pla 2010)');
INSERT INTO `grau` VALUES (7, 'grau en Biotecnologia (Pla 2015)');
INSERT INTO `grau` VALUES (8, 'grau en Ciències Ambientals (Pla 2009)');
INSERT INTO `grau` VALUES (9, 'grau en Matemàtiques (Pla 2010)');
INSERT INTO `grau` VALUES (10, 'grau en Química (Pla 2009)');
 
/* `assignatura` */
INSERT INTO `assignatura` VALUES (1, 'Àlgegra lineal i matemàtica discreta', 6, 'bàsica', 1, 1, 3, 4);
INSERT INTO `assignatura` VALUES (2, 'Càlcul', 6, 'bàsica', 1, 1, 14, 4);
INSERT INTO `assignatura` VALUES (3, 'Física per a informàtica', 6, 'bàsica', 1, 1, 3, 4);
INSERT INTO `assignatura` VALUES (4, 'Introducció a la programació', 6, 'bàsica', 1, 1, 14, 4);
INSERT INTO `assignatura` VALUES (5, 'Organització i gestió d''empreses', 6, 'bàsica', 1, 1, 3, 4);
INSERT INTO `assignatura` VALUES (6, 'Estadística', 6, 'bàsica', 1, 2, 14, 4);
INSERT INTO `assignatura` VALUES (7, 'Estructura i tecnologia de computadors', 6, 'bàsica', 1, 2, 3, 4);
INSERT INTO `assignatura` VALUES (8, 'Fonaments d''electrònica', 6, 'bàsica', 1, 2, 14, 4);
INSERT INTO `assignatura` VALUES (9, 'Lògica i algorísmica', 6, 'bàsica', 1, 2, 3, 4);
INSERT INTO `assignatura` VALUES (10, 'Metodologia de la programació', 6, 'bàsica', 1, 2, 14, 4);
INSERT INTO `assignatura` VALUES (11, 'Arquitectura de Computadors', 6, 'bàsica', 2, 1, 3, 4);
INSERT INTO `assignatura` VALUES (12, 'Estructura de Dades i Algorismes I', 6, 'obligatòria', 2, 1, 3, 4);
INSERT INTO `assignatura` VALUES (13, 'Enginyeria del Programari', 6, 'obligatòria', 2, 1, 14, 4);
INSERT INTO `assignatura` VALUES (14, 'Sistemes Intel·ligents', 6, 'obligatòria', 2, 1, 3, 4);
INSERT INTO `assignatura` VALUES (15, 'Sistemes Operatius', 6, 'obligatòria', 2, 1, 14, 4);
INSERT INTO `assignatura` VALUES (16, 'Bases de Dades', 6, 'bàsica', 2, 2, 14, 4);
INSERT INTO `assignatura` VALUES (17, 'Estructura de Dades i Algorismes II', 6, 'obligatòria', 2, 2, 14, 4);
INSERT INTO `assignatura` VALUES (18, 'Fonaments de Xarxes de Computadors', 6 ,'obligatòria', 2, 2, 3, 4);
INSERT INTO `assignatura` VALUES (19, 'Planificació i Gestió de Projectes Informàtics', 6, 'obligatòria', 2, 2, 3, 4);
INSERT INTO `assignatura` VALUES (20, 'Programació de Serveis Programari', 6, 'obligatòria', 2, 2, 14, 4);
INSERT INTO `assignatura` VALUES (21, 'Desenvolupament d''interfícies d''usuari', 6, 'obligatòria', 3, 1, 14, 4);
INSERT INTO `assignatura` VALUES (22, 'Enginyeria de Requisits', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (23, 'Integració de les Tecnologies de la Informació a les Organitzacions', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (24, 'Modelat i Disseny del Programari 1', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (25, 'Multiprocessadors', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (26, 'Seguretat i compliment normatiu', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (27, 'Sistema d''Informació per a les Organitzacions', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (28, 'Tecnologies web', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (29, 'Teoria de codis i criptografia', 6, 'optativa', 3, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (30, 'Administració de bases de dades', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (31, 'Eines i Mètodes d''Enginyeria del Programari', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (32, 'Informàtica industrial i robòtica', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (33, 'Enginyeria de Sistemes d''Informació', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (34, 'Modelat i Disseny del Programari 2', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (35, 'Negoci Electrònic', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (36, 'Perifèrics i interfícies', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (37, 'Sistemes de temps real', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (38, 'Tecnologies d''accés a xarxa', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (39, 'Tractament digital d''imatges', 6, 'optativa', 3, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (40, 'Administració de xarxes i sistemes operatius', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (41, 'Magatzems de Dades', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (42, 'Fiabilitat i Gestió de Riscos', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (43, 'Línies de Productes Software', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (44, 'Processos d''Enginyeria del Programari 1', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (45, 'Tecnologies multimèdia', 6, 'optativa', 4, 1, NULL, 4);
INSERT INTO `assignatura` VALUES (46, 'Anàlisi i planificació de les TI', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (47, 'Desenvolupament Ràp`id` d''Aplicacions', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (48, 'Gestió de la Qualitat i de la Innovació Tecnològica', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (49, 'Intel·ligència del Negoci', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (50, 'Processos d''Enginyeria del Programari 2', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (51, 'Seguretat Informàtica', 6, 'optativa', 4, 2, NULL, 4);
INSERT INTO `assignatura` VALUES (52, 'Biologia cel·lular', 6, 'bàsica', 1, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (53, 'Física', 6, 'bàsica', 1, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (54, 'Matemàtiques I', 6, 'bàsica', 1, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (55, 'Química general', 6, 'bàsica', 1, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (56, 'Química orgànica', 6, 'bàsica', 1, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (57, 'Biologia vegetal i animal', 6, 'bàsica', 1, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (58, 'Bioquímica', 6, 'bàsica', 1, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (59, 'Genètica', 6, 'bàsica', 1, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (60, 'Matemàtiques II', 6, 'bàsica', 1, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (61, 'Microbiologia', 6, 'bàsica', 1, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (62, 'Botànica agrícola', 6, 'obligatòria', 2, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (63, 'Fisiologia vegetal', 6, 'obligatòria', 2, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (64, 'Genètica molecular', 6, 'obligatòria', 2, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (65, 'Enginyeria bioquímica', 6, 'obligatòria', 2, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (66, 'Termodinàmica i cinètica química aplicada', 6, 'obligatòria', 2, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (67, 'Bioreactors', 6, 'obligatòria', 2, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (68, 'Biotecnologia microbiana', 6, 'obligatòria', 2, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (69, 'Enginyeria genètica', 6, 'obligatòria', 2, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (70, 'Immunologia', 6, 'obligatòria', 2, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (71, 'Virologia', 6, 'obligatòria', 2, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (72, 'Bases moleculars del desenvolupament vegetal', 4.5, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (73, 'Fisiologia animal', 4.5, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (74, 'Metabolisme i biosíntesi de biomolècules', 6, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (75, 'Operacions de separació', 6, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (76, 'Patologia molecular de plantes', 4.5, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (77, 'Tècniques instrumentals bàsiques', 4.5, 'obligatòria', 3, 1, NULL, 7);
INSERT INTO `assignatura` VALUES (78, 'Bioinformàtica', 4.5, 'obligatòria', 3, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (79, 'Biotecnologia dels productes hortofructícules', 4.5, 'obligatòria', 3, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (80, 'Biotecnologia vegetal', 6, 'obligatòria', 3, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (81, 'Genòmica i proteòmica', 4.5, 'obligatòria', 3, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (82, 'Processos biotecnològics', 6, 'obligatòria', 3, 2, NULL, 7);
INSERT INTO `assignatura` VALUES (83, 'Tècniques instrumentals avançades', 4.5, 'obligatòria', 3, 2, NULL, 7);

/* curs escolar */
INSERT INTO `curs_escolar` VALUES (1, 2014, 2015);
INSERT INTO `curs_escolar` VALUES (2, 2015, 2016);
INSERT INTO `curs_escolar` VALUES (3, 2016, 2017);
INSERT INTO `curs_escolar` VALUES (4, 2017, 2018);
INSERT INTO `curs_escolar` VALUES (5, 2018, 2019);

/* alumne se matricula en `assignatura` */
insert into universitat.alumne_es_matricula_assignatura values (1,1,1);
insert into universitat.alumne_es_matricula_assignatura values (2,1,1);
insert into universitat.alumne_es_matricula_assignatura values (4,1,1);
insert into universitat.alumne_es_matricula_assignatura values (19,1,4);
insert into universitat.alumne_es_matricula_assignatura values (23,1,4);
insert into universitat.alumne_es_matricula_assignatura values (24,1,4);
insert into universitat.alumne_es_matricula_assignatura values (1,2,1);
insert into universitat.alumne_es_matricula_assignatura values (2,2,1);
insert into universitat.alumne_es_matricula_assignatura values (4,2,1);
insert into universitat.alumne_es_matricula_assignatura values (19,2,4);
insert into universitat.alumne_es_matricula_assignatura values (23,2,4);
insert into universitat.alumne_es_matricula_assignatura values (24,2,4);
insert into universitat.alumne_es_matricula_assignatura values (1,3,1);
insert into universitat.alumne_es_matricula_assignatura values (2,3,1);
insert into universitat.alumne_es_matricula_assignatura values (4,3,1);
insert into universitat.alumne_es_matricula_assignatura values (19,3,4);
insert into universitat.alumne_es_matricula_assignatura values (23,3,4);
insert into universitat.alumne_es_matricula_assignatura values (24,3,4);
insert into universitat.alumne_es_matricula_assignatura values (19,4,4);
insert into universitat.alumne_es_matricula_assignatura values (23,4,4);
insert into universitat.alumne_es_matricula_assignatura values (24,4,4);
insert into universitat.alumne_es_matricula_assignatura values (19,5,4);
insert into universitat.alumne_es_matricula_assignatura values (23,5,4);
insert into universitat.alumne_es_matricula_assignatura values (24,5,4);
insert into universitat.alumne_es_matricula_assignatura values (19,6,4);
insert into universitat.alumne_es_matricula_assignatura values (23,6,4);
insert into universitat.alumne_es_matricula_assignatura values (24,6,4);
insert into universitat.alumne_es_matricula_assignatura values (19,7,4);
insert into universitat.alumne_es_matricula_assignatura values (23,7,4);
insert into universitat.alumne_es_matricula_assignatura values (24,7,4);
insert into universitat.alumne_es_matricula_assignatura values (19,8,4);
insert into universitat.alumne_es_matricula_assignatura values (23,8,4);
insert into universitat.alumne_es_matricula_assignatura values (24,8,4);
insert into universitat.alumne_es_matricula_assignatura values (19,9,4);
insert into universitat.alumne_es_matricula_assignatura values (23,9,4);
insert into universitat.alumne_es_matricula_assignatura values (24,9,4);
insert into universitat.alumne_es_matricula_assignatura values (19,10,4);
insert into universitat.alumne_es_matricula_assignatura values (23,10,4);
insert into universitat.alumne_es_matricula_assignatura values (24,10,4);
insert into universitat.alumne_es_matricula_assignatura values (1,11,2);
insert into universitat.alumne_es_matricula_assignatura values (2,11,2);
insert into universitat.alumne_es_matricula_assignatura values (4,11,2);
insert into universitat.alumne_es_matricula_assignatura values (19,11,5);
insert into universitat.alumne_es_matricula_assignatura values (23,11,5);
insert into universitat.alumne_es_matricula_assignatura values (24,11,5);
insert into universitat.alumne_es_matricula_assignatura values (1,12,2);
insert into universitat.alumne_es_matricula_assignatura values (2,12,2);
insert into universitat.alumne_es_matricula_assignatura values (4,12,2);
insert into universitat.alumne_es_matricula_assignatura values (19,12,5);
insert into universitat.alumne_es_matricula_assignatura values (23,12,5);
insert into universitat.alumne_es_matricula_assignatura values (24,12,5);
insert into universitat.alumne_es_matricula_assignatura values (1,13,2);
insert into universitat.alumne_es_matricula_assignatura values (2,13,2);
insert into universitat.alumne_es_matricula_assignatura values (4,13,2);
insert into universitat.alumne_es_matricula_assignatura values (19,13,5);
insert into universitat.alumne_es_matricula_assignatura values (23,13,5);
insert into universitat.alumne_es_matricula_assignatura values (24,13,5);
insert into universitat.alumne_es_matricula_assignatura values (1,14,2);
insert into universitat.alumne_es_matricula_assignatura values (2,14,2);
insert into universitat.alumne_es_matricula_assignatura values (4,14,2);
insert into universitat.alumne_es_matricula_assignatura values (19,14,5);
insert into universitat.alumne_es_matricula_assignatura values (23,14,5);
insert into universitat.alumne_es_matricula_assignatura values (24,14,5);
insert into universitat.alumne_es_matricula_assignatura values (1,15,2);
insert into universitat.alumne_es_matricula_assignatura values (2,15,2);
insert into universitat.alumne_es_matricula_assignatura values (4,15,2);
insert into universitat.alumne_es_matricula_assignatura values (19,15,5);
insert into universitat.alumne_es_matricula_assignatura values (23,15,5);
insert into universitat.alumne_es_matricula_assignatura values (24,15,5);
insert into universitat.alumne_es_matricula_assignatura values (1,16,2);
insert into universitat.alumne_es_matricula_assignatura values (2,16,2);
insert into universitat.alumne_es_matricula_assignatura values (4,16,2);
insert into universitat.alumne_es_matricula_assignatura values (19,16,5);
insert into universitat.alumne_es_matricula_assignatura values (23,16,5);
insert into universitat.alumne_es_matricula_assignatura values (24,16,5);
insert into universitat.alumne_es_matricula_assignatura values (1,17,2);
insert into universitat.alumne_es_matricula_assignatura values (2,17,2);
insert into universitat.alumne_es_matricula_assignatura values (4,17,2);
insert into universitat.alumne_es_matricula_assignatura values (19,17,5);
insert into universitat.alumne_es_matricula_assignatura values (23,17,5);
insert into universitat.alumne_es_matricula_assignatura values (24,17,5);
insert into universitat.alumne_es_matricula_assignatura values (1,18,2);
insert into universitat.alumne_es_matricula_assignatura values (2,18,2);
insert into universitat.alumne_es_matricula_assignatura values (4,18,2);
insert into universitat.alumne_es_matricula_assignatura values (19,18,5);
insert into universitat.alumne_es_matricula_assignatura values (23,18,5);
insert into universitat.alumne_es_matricula_assignatura values (24,18,5);
insert into universitat.alumne_es_matricula_assignatura values (1,19,2);
insert into universitat.alumne_es_matricula_assignatura values (2,19,2);
insert into universitat.alumne_es_matricula_assignatura values (4,19,2);
insert into universitat.alumne_es_matricula_assignatura values (19,19,5);
insert into universitat.alumne_es_matricula_assignatura values (23,19,5);
insert into universitat.alumne_es_matricula_assignatura values (24,19,5);
insert into universitat.alumne_es_matricula_assignatura values (1,20,2);
insert into universitat.alumne_es_matricula_assignatura values (2,20,2);
insert into universitat.alumne_es_matricula_assignatura values (4,20,2);
insert into universitat.alumne_es_matricula_assignatura values (19,20,5);
insert into universitat.alumne_es_matricula_assignatura values (23,20,5);
insert into universitat.alumne_es_matricula_assignatura values (24,20,5);
insert into universitat.alumne_es_matricula_assignatura values (9,52,1);
insert into universitat.alumne_es_matricula_assignatura values (11,52,1);
insert into universitat.alumne_es_matricula_assignatura values (15,52,1);
insert into universitat.alumne_es_matricula_assignatura values (22,52,1);
insert into universitat.alumne_es_matricula_assignatura values (9,53,1);
insert into universitat.alumne_es_matricula_assignatura values (11,53,1);
insert into universitat.alumne_es_matricula_assignatura values (15,53,1);
insert into universitat.alumne_es_matricula_assignatura values (22,53,1);
insert into universitat.alumne_es_matricula_assignatura values (9,54,1);
insert into universitat.alumne_es_matricula_assignatura values (11,54,1);
insert into universitat.alumne_es_matricula_assignatura values (15,54,1);
insert into universitat.alumne_es_matricula_assignatura values (22,54,1);
insert into universitat.alumne_es_matricula_assignatura values (9,55,1);
insert into universitat.alumne_es_matricula_assignatura values (11,55,1);
insert into universitat.alumne_es_matricula_assignatura values (15,55,1);
insert into universitat.alumne_es_matricula_assignatura values (22,55,1);
insert into universitat.alumne_es_matricula_assignatura values (9,56,1);
insert into universitat.alumne_es_matricula_assignatura values (11,56,1);
insert into universitat.alumne_es_matricula_assignatura values (15,56,1);
insert into universitat.alumne_es_matricula_assignatura values (22,56,1);
insert into universitat.alumne_es_matricula_assignatura values (9,57,1);
insert into universitat.alumne_es_matricula_assignatura values (11,57,1);
insert into universitat.alumne_es_matricula_assignatura values (15,57,1);
insert into universitat.alumne_es_matricula_assignatura values (22,57,1);
insert into universitat.alumne_es_matricula_assignatura values (9,58,1);
insert into universitat.alumne_es_matricula_assignatura values (11,58,1);
insert into universitat.alumne_es_matricula_assignatura values (15,58,1);
insert into universitat.alumne_es_matricula_assignatura values (22,58,1);
insert into universitat.alumne_es_matricula_assignatura values (9,59,1);
insert into universitat.alumne_es_matricula_assignatura values (11,59,1);
insert into universitat.alumne_es_matricula_assignatura values (15,59,1);
insert into universitat.alumne_es_matricula_assignatura values (22,59,1);
insert into universitat.alumne_es_matricula_assignatura values (9,60,1);
insert into universitat.alumne_es_matricula_assignatura values (11,60,1);
insert into universitat.alumne_es_matricula_assignatura values (15,60,1);
insert into universitat.alumne_es_matricula_assignatura values (22,60,1);
insert into universitat.alumne_es_matricula_assignatura values (9,61,1);
insert into universitat.alumne_es_matricula_assignatura values (11,61,1);
insert into universitat.alumne_es_matricula_assignatura values (15,61,1);
insert into universitat.alumne_es_matricula_assignatura values (22,61,1);
