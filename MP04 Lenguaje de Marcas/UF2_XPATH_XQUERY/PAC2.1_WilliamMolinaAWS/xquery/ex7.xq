(:
7 - Muestra los bailes que tengan una duracion (fin - comienzo) de mas de 250 dias. (Pista: days-from-duration)
:)

for $baile in doc("bailes.xml")/bailes/baile

let $dias := xs:date($baile/fin) - xs:date($baile/comienzo)
where days-from-duration($dias) > 250

return concat ("Nombre: ",$baile/nombre/text())
