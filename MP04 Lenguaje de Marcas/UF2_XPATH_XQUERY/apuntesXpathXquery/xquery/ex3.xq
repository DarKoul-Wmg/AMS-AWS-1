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