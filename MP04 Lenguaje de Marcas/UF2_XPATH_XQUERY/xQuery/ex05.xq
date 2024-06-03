for $articulo in doc("../xQuery/ejercicios0xquery.xml")//articulos/articulo/contenido/text()

where contains($articulo,"presidenta")
return $articulo