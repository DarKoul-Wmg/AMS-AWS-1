for $x in doc("pagina.xml")/pagina/articulos/articulo
let $fechas := doc("pagina.xml")/pagina/articulos/articulo/fecha
where $x/fecha = max(for $date in $fechas return xs:date($date))
return concat("El titulo mas reciente es: '", $x/titulo, "'")