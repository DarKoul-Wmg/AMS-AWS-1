

let $contenido := doc("pagina.xml")/pagina/articulos/articulo/contenido
let $totalPalabras := sum(
  for $c in $contenido 
  return count(tokenize($c, '\s+')))
let $totalArticulos := count( $contenido)
return concat("Avg: ", $totalPalabras div $totalArticulos)