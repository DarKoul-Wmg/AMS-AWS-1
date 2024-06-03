for $articulo in doc("../xQuery/ejercicios0xquery.xml")//articulo
order by $articulo/fecha descending
return concat($articulo/titulo/text()," - ", $articulo/fecha)
  