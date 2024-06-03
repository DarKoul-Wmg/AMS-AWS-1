for $x in doc("pagina.xml")/pagina/articulos/articulo
let $a := $x/autor
where $x/fecha > "2022-09-03"
group by $a
return concat("", $x/autor, "")