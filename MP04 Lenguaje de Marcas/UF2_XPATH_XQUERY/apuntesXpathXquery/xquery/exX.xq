(:
  Muestra los libros ordenados primero por "category" y luego por "title" en una sola consulta. (Formato: <title>titulo</title>)
:)
for $book in doc("../xquery/books.xml")/bookstore/book
order by $book/caategory, $book/title
return <title>{$book/title/text()}</title>

(:
Muestra el precio mínimo y máximo de los libros. (Formato: <min>x</min><max>y</max>)
:)
let $books := doc("../xquery/books.xml")/bookstore/book
let $min := min($books/price)
let $max := max($books/price)

return <result>
<min>{$min}</min>
<max>{$max}</max>
</result>

(:
Muestra el título del libro, su precio y su precio sin el IVA incluido. Ordénalos por precio. (Formato: <title>titulo</title> <price>precio</price> <price_woIVA>precio</price_woIVA>)
:)
for $book in doc("../xquery/books.xml")/bookstore/book
let $woIVA := round($book/price div 1.21,2)
order by $book/price

return <result>
<title> {$book/title/text()}</title> 
<price>{$book/price}</price> 
<price_woIVA>{$woIVA}</price_woIVA>
</result>  

(:
  Muestra la suma total de los precios de los libros. (Formato: <total_sum>suma</total_sum>)
:)
let $books :=doc("books.xml")/bookstore/book
let $total_price := round(sum($books/price),2)
return <total_sum>{$total_price}</total_sum>

(:
  Muestra en la misma etiqueta el título y entre paréntesis el número de autores que tiene ese título. (Formato: <title>titulo(x)</title>)
:)
let $books := doc("books.xml")/bookstore/book
for $book in $books
  let $title := $book/title/text()
  let $num_author := count($book/author)
 
return <title>{$title} ({$num_author})</title>

(:
  Muestra los libros cuya categoría empiece por "C". (Formato: <title category="categoria">titulo</title>)
:)

let $books := doc("books.xml")/bookstore/book
for $book in $books
  where starts-with($book/@category, "c")
  let $title := $book/title
  let $category := $book/@category

return <title category="{$category}">{$title}</title>

(:
  Muestra los libros que tengan una "X" mayúscula o minúscula en el título ordenados de manera descendente. (Formato: <title>titulo</title>)
:)
for $book in doc("books.xml")/bookstore/book[contains(title,"X") or contains(title,"x")]
order by $book/title descending
return <title>{$book/title/text()}</title>