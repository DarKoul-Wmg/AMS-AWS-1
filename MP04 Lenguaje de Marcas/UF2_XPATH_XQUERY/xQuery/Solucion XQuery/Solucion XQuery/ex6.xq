let $autores := distinct-values(doc("pagina.xml")/pagina/articulos/articulo/autor)
for $autor in $autores
let $articulos := distinct-values(doc("pagina.xml")/pagina/articulos/articulo[autor = $autor])
let $numArticulos := count($articulos)
where  $numArticulos = max(
  for $a in $autores
  let $ar := distinct-values(doc("pagina.xml")/pagina/articulos/articulo[autor = $a])
  let $n := count($ar)
  return $n
)
return concat("Author with most articles: ", $autor)