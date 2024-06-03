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

