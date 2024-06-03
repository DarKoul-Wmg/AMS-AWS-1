let $articulos := doc("pagina.xml")/pagina/articulos/articulo
let $fechas := $articulos/fecha/xs:date(.)
return concat("Min: ", min($fechas), ", Max: ", max($fechas))