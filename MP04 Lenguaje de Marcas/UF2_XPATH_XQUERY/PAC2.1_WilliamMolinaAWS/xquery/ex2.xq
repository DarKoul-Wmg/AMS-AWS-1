(:
2 - Mostrar la media de los precios de todos los bailes.
:)


let $precio_total := sum(doc('bailes.xml')/bailes/baile/precio)
let $bailes_count := count(doc('bailes.xml')/bailes/baile)

let $media_precio := $precio_total div $bailes_count

return concat("Precio medio = ",$media_precio)