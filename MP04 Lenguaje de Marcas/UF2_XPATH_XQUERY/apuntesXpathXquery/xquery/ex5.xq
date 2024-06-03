(:
  Muestra en la misma etiqueta el título y entre paréntesis el número de autores que tiene ese título. (Formato: <title>titulo(x)</title>)
:)
let $books := doc("books.xml")/bookstore/book
for $book in $books
  let $title := $book/title/text()
  let $num_author := count($book/author)
 
return <title>{$title} ({$num_author})</title>