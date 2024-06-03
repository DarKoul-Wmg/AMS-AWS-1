let $total_palabras:= sum(
         for $articulo in doc("../xQuery/ejercicios0xquery.xml")//articulo
         return count(tokenize($articulo/contenido, "\s+")))
         
let $total_articulos := count(doc("../xQuery/ejercicios0xquery.xml")//articulo)
let $media_palabras := $total_palabras div $total_articulos

return $media_palabras


