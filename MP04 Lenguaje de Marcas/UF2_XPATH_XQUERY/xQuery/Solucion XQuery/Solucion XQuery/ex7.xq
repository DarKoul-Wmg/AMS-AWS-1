for $x in doc("pagina.xml")/pagina/articulos/articulo
order by $x/fecha descending
return concat("-", $x/titulo, " (" , $x/fecha, ")")