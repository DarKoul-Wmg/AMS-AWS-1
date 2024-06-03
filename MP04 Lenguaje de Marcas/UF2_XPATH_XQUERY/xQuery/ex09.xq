for $categoria in distinct-values (doc ("../xQuery/ejercicios0xquery.xml")//articulo/@categoria)
return concat($categoria, "tiene ",articulo[@categoria = $categoria])

  
