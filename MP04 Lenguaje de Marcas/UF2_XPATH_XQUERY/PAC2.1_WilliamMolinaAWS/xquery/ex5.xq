(:
5 - Mostrar cuántas plazas en total oferta el profesor "Jesus Lozano".
:)

let $plazas_totales := sum(doc("bailes.xml")/bailes/baile[profesor = "Jesus Lozano"]/plazas)

return concat("Plazas totales de Jesus Lozano: ", $plazas_totales)