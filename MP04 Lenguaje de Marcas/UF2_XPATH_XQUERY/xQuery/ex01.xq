for $articulo in doc("../xQuery/ejercicios0xquery.xml")/pagina/articulos/articulo
return $articulo/titulo/text()