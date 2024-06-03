(:
3 - Muestra el nombre del baile, su precio y el precio con un descuento del 15% para familias numerosas. Ordenar por el nombre del baile.
:)

for $baile in doc("bailes.xml")/bailes/baile

let $desc15 := $baile/precio -($baile/precio * 0.15)
order by $baile/nombre

return concat("Baile: ",$baile/nombre," - precio: ",$baile/precio," - precio descuento: ",$desc15) 