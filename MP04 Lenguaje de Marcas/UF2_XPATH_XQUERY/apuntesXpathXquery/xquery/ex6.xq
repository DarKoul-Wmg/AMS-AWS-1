(:
  Muestra los libros cuya categoría empiece por "C". (Formato: <title category="categoria">titulo</title>)
:)

let $books := doc("books.xml")/bookstore/book
for $book in $books
  where starts-with($book/@category, "c")
  let $title := $book/title
  let $category := $book/@category

return <title category="{$category}">{$title}</title>