let $x := doc("pagina.xml")/pagina/articulos/articulo
return concat("There are ", count($x/titulo), " articles.")