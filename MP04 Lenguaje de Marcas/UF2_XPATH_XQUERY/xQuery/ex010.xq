let $fechas := doc("../xQuery/ejercicios0xquery.xml")//articulo/fecha/data()
let $fecha_antigua := min(for $fecha in $fechas return xs:date($fecha))
let $fecha_reciente := max(for $fecha in $fechas return xs:date($fecha))

return concat("Fecha min: ",$fecha_antigua," - ","Fecha max: ",$fecha_reciente)
