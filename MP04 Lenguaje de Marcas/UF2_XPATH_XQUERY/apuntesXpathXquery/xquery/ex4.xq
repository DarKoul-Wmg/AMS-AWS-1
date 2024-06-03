(:
  Muestra la suma total de los precios de los libros. (Formato: <total_sum>suma</total_sum>)
:)
let $books :=doc("books.xml")/bookstore/book

let $total_price := round(sum($books/price),2)

return <total_sum>{$total_price}</total_sum>