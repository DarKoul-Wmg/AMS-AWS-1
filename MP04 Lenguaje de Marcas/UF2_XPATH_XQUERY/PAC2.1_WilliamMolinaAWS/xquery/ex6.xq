(:
6 - Muestra los bailes que tengan una "S" mayúscula o minúscula en el título ordenados de manera descendente.
:)

for $baile in doc("bailes.xml")/bailes/baile[contains(nombre,"S") or contains(nombre,"s")]

order by $baile/nombre descending

return $baile/nombre/text()