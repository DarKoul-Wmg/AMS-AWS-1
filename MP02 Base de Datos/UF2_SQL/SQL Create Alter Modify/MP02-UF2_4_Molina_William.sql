-- 1 
SELECT nom_alumne, concat(cognom1_alumne, cognom2_alumne) as cognoms
from v_alumnes_assignatures
where inici_curs_escolar = '2015' 
	AND fi_curs_escolar = '2016' 
    AND curs_assignatura = 'segon';

-- 2
SELECT DISTINCT nom_assignatura, id_assignatura as id, g.nom as nom_grau
FROM v_alumnes_assignatures aa
JOIN grau g ON aa.id_grau = g.id
WHERE curs_assignatura = 'primer' AND g.nom ='grau en Biotecnologia (Pla 2015)';

-- 3
SELECT count(*) as quantitat_alumnes
FROM (SELECT distinct aa.id_alumne 
	FROM v_alumnes_assignatures aa
	JOIN grau g ON aa.id_grau = g.id
	WHERE g.nom = 'grau en Biotecnologia (Pla 2015)' 
	AND aa.inici_curs_escolar = '2014'
	AND aa.fi_curs_escolar = '2015') as alumnes; 