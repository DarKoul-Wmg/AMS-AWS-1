(:
4 - Muestra el dinero que ganaría en un mes la profesora "Laura" (no conocemos su apellido) si se completaran todas las plazas de su baile.
:)

let $precioMensual := doc("bailes.xml")/bailes/baile[contains(profesor,"Laura")]/precio
let $plazasDisponibles := doc("bailes.xml")/bailes/baile[contains(profesor,"Laura")]/plazas

let $precio_total := $precioMensual * $plazasDisponibles

return concat("Ganancia mensual: ",$precio_total)
