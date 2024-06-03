for $x in doc("pagina.xml")/pagina/articulos/articulo
where contains($x/contenido, "presidenta") or contains($x/titulo, "presidenta")
order by $x/titulo
return concat("- ", $x/titulo, "")