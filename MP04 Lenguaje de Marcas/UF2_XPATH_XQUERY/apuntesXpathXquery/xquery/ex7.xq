(:
  Muestra los libros que tengan una "X" mayúscula o minúscula en el título ordenados de manera descendente. (Formato: <title>titulo</title>)
:)
for $book in doc("books.xml")/bookstore/book[contains(title,"X") or contains(title,"x")]
order by $book/title descending
return <title>{$book/title/text()}</title>