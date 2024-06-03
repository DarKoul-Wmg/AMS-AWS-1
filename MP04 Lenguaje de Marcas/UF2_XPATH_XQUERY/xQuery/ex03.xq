for $articulo in doc("../xQuery/ejercicios0xquery.xml")/pagina/articulos/articulo

where $articulo/fecha > "2022-09-03"
return $articulo/autor/text()

(:
for $x in doc("../xQuery/ejercicios0xquery.xml")/pagina/articulos/articulo
let $a:= $x/autor

where $x/fecha > "2022-09-03"
group by $a
return $x/autor/
:)
