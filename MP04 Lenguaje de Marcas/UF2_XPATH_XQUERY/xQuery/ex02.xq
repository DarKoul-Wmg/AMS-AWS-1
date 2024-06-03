let $articulos := doc("../xQuery/ejercicios0xquery.xml")/pagina/articulos/articulo
return concat("Hay ",count($articulos)," articulos")