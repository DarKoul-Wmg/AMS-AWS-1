let $categorias := distinct-values(doc("pagina.xml")/pagina/articulos/articulo/@categoria)
for $categoria in $categorias
let $articulos := (doc("pagina.xml")/pagina/articulos/articulo[@categoria = $categoria])
let $numArticulos := count($articulos)
return concat($categoria, " tiene ", $numArticulos, " articulos.")