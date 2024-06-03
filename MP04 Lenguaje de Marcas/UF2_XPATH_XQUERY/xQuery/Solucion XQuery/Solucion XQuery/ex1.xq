for $x in doc("pagina.xml")/pagina/articulos/articulo
order by $x/titulo
return concat("-", $x/titulo, "")