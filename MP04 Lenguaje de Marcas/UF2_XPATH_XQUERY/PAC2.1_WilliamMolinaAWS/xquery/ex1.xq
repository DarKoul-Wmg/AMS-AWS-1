(:
1 - Muestra los bailes ordenados primero por "plazas" y luego por "nombre" en una sola consulta.
:)
for $baile in doc('bailes.xml')/bailes/baile
order by xs:integer($baile/plazas),$baile/nombre

return concat ($baile/nombre," - ",$baile/plazas)