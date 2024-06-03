-- ESTO SON LAS SELECT NOTMALES, NO CON VISTAS

-- 4
	-- 4.1
SELECT DISTINCT nom, concat(cognom1 ,cognom2) as cognoms
FROM persona p
JOIN alumne_es_matricula_assignatura ama ON p.id = ama.id_alumne
JOIN curs_escolar ce ON ama.id_curs_escolar = ce.id
WHERE p.tipus ='alumne' AND any_inici = '2014' AND any_fi = '2015';

	-- 4.2
SELECT DISTINCT p.nom, concat(cognom1 ,cognom2) as cognoms, g.id, g.nom as nom_grau
FROM persona p
JOIN alumne_es_matricula_assignatura ama ON p.id = ama.id_alumne
JOIN assignatura a ON ama.id_assignatura = a.id
JOIN grau g ON a.id_grau = g.id
WHERE p.tipus = 'alumne' AND g.nom = 'grau en Biotecnologia (Pla 2015)';

	-- 4.3
SELECT count(*) as quantitat_alumnes
FROM ( SELECT DISTINCT p.id
	   FROM persona p
       JOIN alumne_es_matricula_assignatura ama ON p.id = ama.id_alumne
	   JOIN assignatura a ON ama.id_assignatura = a.id
       JOIN curs_escolar ce ON ama.id_curs_escolar = ce.id
       JOIN grau g ON a.id_grau = g.id
       WHERE p.tipus = 'alumne' AND g.nom = 'grau en Biotecnologia (Pla 2015)' AND ce.any_inici = '2014' AND ce.any_fi = '2015'
)as alumnes; 