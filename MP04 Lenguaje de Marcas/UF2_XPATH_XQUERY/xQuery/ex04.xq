let $document := doc("../xQuery/ejercicios0xquery.xml")
let $fechas := $document//articulo/fecha
let $fechaMasReciente:= max(for $fecha in $fechas return xs:date($fecha))

return $document//articulo[fecha = $fechaMasReciente]/titulo/text()
