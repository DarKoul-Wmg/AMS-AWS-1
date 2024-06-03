(:
  Muestra los libros ordenados primero por "category" y luego por "title" en una sola consulta. (Formato: <title>titulo</title>)
:)
for $book in doc("../xquery/books.xml")/bookstore/book
order by $book/caategory, $book/title
return <title>{$book/title/text()}</title>